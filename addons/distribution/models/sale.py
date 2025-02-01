# -*- coding: utf-8 -*-
# Part of CoreTech Solutions. See LICENSE.txt file for full copyright and licensing details.

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
import re

class Sale(models.Model):
    _name = 'distribution.sale'
    _description = 'Sale'
    _order = 'date desc'
    _inherit = ['mail.thread', 'utm.mixin']

    name = fields.Char(
        string='Order Reference',
        required=True,
        readonly=True,
        index=True,
        copy=False,
        default=lambda self: _('New')
    )
    customer_id = fields.Many2one(
        'distribution.customer', 
        string='Customer', 
        required=True,
        tracking=True,
        index=True
    )
    date = fields.Datetime(
        string='Sale Date', 
        default=fields.Datetime.now, 
        required=True,
        index=True
    )
    total_amount = fields.Float(
        string='Total Amount', 
        compute='_compute_total_amount', 
        store=True,
        currency_field='currency_id',
        digits='Account'
    )
    warehouse_id = fields.Many2one(
        'distribution.warehouse',
        string='Warehouse',
        required=True,
        tracking=True,
        index=True
    )
    order_line_ids = fields.One2many(
        'distribution.order_line', 
        'sale_id', 
        string='Order Lines',
        copy=True
    )
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        required=True,
        default=lambda self: self.env.company.currency_id
    )
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('done', 'Done'),
            ('cancel', 'Cancelled'),
        ],
        string='Status',
        default='draft',
        tracking=True
    )

    @api.depends('order_line_ids.subtotal')
    def _compute_total_amount(self):
        for sale in self:
            sale.total_amount = sum(line.subtotal for line in sale.order_line_ids)

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('distribution.sale') or _('New')
        return super().create(vals)

    def action_confirm(self):
        for order in self:
            order._reserve_stock()
        self.write({'state': 'confirmed'})

    def action_done(self):
        self._update_stock()
        self.write({'state': 'done'})

    def action_cancel(self):
        for order in self:
            if order.state == 'done':
                raise ValidationError(_("You cannot cancel an order that is already marked as Done."))

            for line in order.order_line_ids:
                if line.stock_id:
                    line.stock_id.sudo().write({
                        'reserved_quantity': max(0, line.stock_id.reserved_quantity - line.quantity)
                    })
            order.write({'state': 'cancel'})

    def _reserve_stock(self):
        for order in self:
            if not order.warehouse_id:
                raise ValidationError(_("Select a warehouse before confirming the order."))
            for line in order.order_line_ids:
                if line.quantity > line.product_id._get_available_quantity(order.warehouse_id):
                    raise ValidationError(_(
                        f"Not enough stock for {line.product_id.name}. "
                        f"Available: {line.product_id._get_available_quantity(order.warehouse_id)}, Requested: {line.quantity}"
                    ))
                line.stock_id.reserved_quantity += line.quantity

    def _update_stock(self):
        for order in self:
            for line in order.order_line_ids:
                line.stock_id.sudo().write({
                    'quantity': line.stock_id.quantity - line.quantity,
                    'reserved_quantity': line.stock_id.reserved_quantity - line.quantity
                })

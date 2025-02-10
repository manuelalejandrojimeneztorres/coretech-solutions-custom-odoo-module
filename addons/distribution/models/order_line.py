# -*- coding: utf-8 -*-
# Part of CoreTech Solutions. See LICENSE.txt file for full copyright and licensing details.

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
import re

class OrderLine(models.Model):
    _name = 'distribution.order_line'
    _description = 'Order Line'
    _order = 'product_id, sale_id'

    sale_id = fields.Many2one(
        'distribution.sale', 
        string='Sale', 
        required=True, 
        ondelete='cascade',
        index=True
    )
    product_id = fields.Many2one(
        'distribution.product', 
        string='Product', 
        required=True,
        domain="[('id', 'in', available_product_ids)]"
    )
    stock_id = fields.Many2one(
        'distribution.stock',
        string='Stock Entry',
        compute='_compute_stock_id',
        store=True,
        readonly=False,
        help="Stock entry for the selected product and warehouse"
    )
    quantity = fields.Integer(
        string='Quantity', 
        required=True, 
        default=1,
        tracking=True
    )
    price_unit = fields.Float(
        string='Unit Price', 
        required=True,
        digits='Product Price'
    )
    subtotal = fields.Float(
        string='Subtotal', 
        compute='_compute_subtotal', 
        store=True,
        currency_field='currency_id',
        digits='Account'
    )
    currency_id = fields.Many2one(
        related='sale_id.currency_id',
        string='Currency',
        readonly=True
    )
    available_product_ids = fields.Many2many(
        related='sale_id.warehouse_id.product_ids',
        string='Available Products'
    )

    @api.depends('quantity', 'price_unit')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price_unit

    @api.depends('product_id', 'sale_id.warehouse_id')
    def _compute_stock_id(self):
        for line in self:
            if line.product_id and line.sale_id.warehouse_id:
                line.stock_id = self.env['distribution.stock'].search([
                    ('product_id', '=', line.product_id.id),
                    ('warehouse_id', '=', line.sale_id.warehouse_id.id)
                ], limit=1)
            else:
                line.stock_id = False

    @api.constrains('quantity')
    def _check_positive_quantity(self):
        for line in self:
            if line.quantity <= 0:
                raise ValidationError(_('Order line quantity must be positive.'))

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.price_unit = self.product_id.price

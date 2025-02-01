# -*- coding: utf-8 -*-
# Part of CoreTech Solutions. See LICENSE.txt file for full copyright and licensing details.

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
import re

class Product(models.Model):
    _name = 'distribution.product'
    _description = 'Product'
    _order = 'name asc'
    _inherit = ['image.mixin']

    name = fields.Char(string='Product Name', required=True, index=True)
    description = fields.Text(string='Description', translate=True)
    detailed_description = fields.Html(string='Detailed Description')
    sku = fields.Char(
        string='SKU', 
        required=True, 
        index=True,
        help="Stock Keeping Unit (Unique identifier)"
    )
    price = fields.Float(
        string='Price', 
        required=True,
        digits='Product Price'
    )
    warehouse_ids = fields.Many2many(
        'distribution.warehouse',
        relation='product_warehouse_rel',
        column1='product_id',
        column2='warehouse_id',
        string='Available Warehouses'
    )
    barcode = fields.Char(string='Barcode', copy=False)
    stock_quantity = fields.Integer(
        string='Total Stock',
        compute='_compute_total_stock',
        store=True,
        help='Total stock across all warehouses.'
    )
    stock_ids = fields.One2many(
        'distribution.stock', 
        'product_id', 
        string='Stock per Warehouse'
    )
    order_line_ids = fields.One2many(
        'distribution.order_line', 
        'product_id', 
        string='Order Lines'
    )

    _sql_constraints = [
        ('sku_unique', 'unique(sku)', 'The SKU must be unique.'),
        ('price_positive', 'CHECK(price >= 0)', 'Price must be positive.'),
        ('barcode_unique', 'unique(barcode)', 'Barcode must be unique.')
    ]

    @api.depends('stock_ids.quantity', 'stock_ids.reserved_quantity')
    def _compute_total_stock(self):
        for product in self:
            product.stock_quantity = sum(
                stock.quantity - stock.reserved_quantity 
                for stock in product.stock_ids
            )

    def _get_available_quantity(self, warehouse):
        self.ensure_one()
        stock = self.stock_ids.filtered(lambda s: s.warehouse_id == warehouse)
        return stock.quantity - stock.reserved_quantity if stock else 0

# -*- coding: utf-8 -*-
# Part of CoreTech Solutions. See LICENSE.txt file for full copyright and licensing details.

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
import re

class Stock(models.Model):
    _name = 'distribution.stock'
    _description = 'Stock'
    _order = 'warehouse_id, product_id'

    product_id = fields.Many2one(
        'distribution.product', 
        string='Product', 
        required=True,
        index=True
    )
    warehouse_id = fields.Many2one(
        'distribution.warehouse', 
        string='Warehouse', 
        required=True,
        index=True
    )
    quantity = fields.Integer(
        string='Quantity', 
        required=True, 
        default=0,
        help="Current stock quantity"
    )
    reserved_quantity = fields.Integer(
        string='Reserved',
        default=0,
        help="Quantity reserved for pending orders"
    )
    last_inventory_date = fields.Datetime(string='Last Inventory Date')

    _sql_constraints = [
        ('unique_stock', 'unique(product_id, warehouse_id)', 'Each product must have a unique stock entry per warehouse.'),
        ('quantity_positive', 'CHECK(quantity >= 0)', 'Stock quantity cannot be negative.'),
        ('reserved_positive', 'CHECK(reserved_quantity >= 0)', 'Reserved quantity cannot be negative.')
    ]

    def name_get(self):
        return [(record.id, f"{record.product_id.name} - {record.warehouse_id.name}") for record in self]

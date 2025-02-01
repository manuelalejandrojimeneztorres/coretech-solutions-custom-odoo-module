# -*- coding: utf-8 -*-
# Part of CoreTech Solutions. See LICENSE.txt file for full copyright and licensing details.

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
import re

class Warehouse(models.Model):
    _name = 'distribution.warehouse'
    _description = 'Warehouse'
    _order = 'name asc'

    name = fields.Char(string='Warehouse Name', required=True, index=True)
    code = fields.Char(string='Short Code', size=5, required=True)
    location = fields.Char(string='Location')
    product_ids = fields.Many2many(
        'distribution.product',
        string='Available Products',
        relation='product_warehouse_rel',
        column1='warehouse_id',
        column2='product_id'
    )
    manager_id = fields.Many2one(
        'res.users', 
        string='Manager',
        tracking=True
    )
    capacity = fields.Integer(
        string='Capacity', 
        help='Total storage capacity in cubic meters',
        required=True
    )
    active = fields.Boolean(string='Active', default=True)
    company_id = fields.Many2one(
        'res.company', 
        string='Company',
        default=lambda self: self.env.company
    )
    stock_ids = fields.One2many(
        'distribution.stock', 
        'warehouse_id', 
        string='Stock'
    )

    _sql_constraints = [
        ('capacity_positive', 'CHECK(capacity >= 0)', 'Capacity must be positive.'),
        ('code_unique', 'unique(code)', 'Warehouse code must be unique.')
    ]

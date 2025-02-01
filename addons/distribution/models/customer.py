# -*- coding: utf-8 -*-
# Part of CoreTech Solutions. See LICENSE.txt file for full copyright and licensing details.

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
import re

class Customer(models.Model):
    _name = 'distribution.customer'
    _description = 'Customer'
    _order = 'name asc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    email = fields.Char(
        string='Email', 
        required=True, 
        tracking=True,
        index=True
    )
    phone = fields.Char(string='Phone', tracking=True)
    address = fields.Text(string='Address')
    vat = fields.Char(
        string='VAT Number', 
        tracking=True,
        help="Tax Identification Number. Include country code."
    )
    active = fields.Boolean(string='Active', default=True, tracking=True)
    image_1920 = fields.Image("Image")
    sale_ids = fields.One2many(
        'distribution.sale',
        'customer_id',
        string='Sales Orders'
    )

    _sql_constraints = [
        ('email_unique', 'unique(email)', 'The email must be unique.'),
        ('vat_unique', 'unique(vat)', 'The VAT number must be unique.')
    ]

    @api.constrains('email')
    def _check_email_format(self):
        for record in self:
            if not re.match(r"[^@]+@[^@]+\.[^@]+", record.email):
                raise ValidationError(_('Invalid email format'))

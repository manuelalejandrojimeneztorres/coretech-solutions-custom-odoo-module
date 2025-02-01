# -*- coding: utf-8 -*-
# Part of CoreTech Solutions. See LICENSE.txt file for full copyright and licensing details.

{
    'name': "CoreTech Distribution",
    'version': '1.0',
    'author': "CoreTech Solutions",
    'website': "https://www.coretechsolutions.com",
    'category': 'Inventory/Management',
    'summary': "Module for managing electronic and IT components distribution.",
    'description': """
CoreTech Distribution
======================
Manage customers, warehouses, products, sales, and stock efficiently.
Includes features for order management, inventory tracking, and role-based access control.
    """,
    'depends': ['base', 'sale', 'stock', 'mail'],
    'data': [
        'data/actions_data.xml',
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'data/menu_coretech_data.xml',
        'views/actions_data.xml',
        'views/customer_views.xml',
        'views/warehouse_views.xml',
        'views/product_views.xml',
        'views/sale_views.xml',
        'views/stock_views.xml',
        'views/order_line_views.xml'
    ],
    'demo': [
        'demo/customer_demo.xml',
        'demo/product_demo.xml',
        'demo/sale_demo.xml'
    ],
    'icon': 'distribution/static/description/icon.png',
    # 'assets': {
    #     'web.assets_backend': [
    #         'distribution/static/src/css/styles.css',
    #     ],
    #     'web.assets_frontend': [
    #         'distribution/static/src/css/styles.css',
    #     ]
    # },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}

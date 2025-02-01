# -*- coding: utf-8 -*-
# Part of CoreTech Solutions. See LICENSE.txt file for full copyright and licensing details.

# from odoo import http
# from odoo.http import request

# class DistributionController(http.Controller):

#     @http.route('/distribution/check_stock', type='json', auth='user')
#     def check_stock(self, product_id, warehouse_id):
#         """
#         Verifies the available stock of a product in a specific warehouse.
#         """
#         Product = request.env['product.product'].sudo()
#         Warehouse = request.env['stock.warehouse'].sudo()

#         product = Product.browse(product_id)
#         warehouse = Warehouse.browse(warehouse_id)

#         if not product.exists() or not warehouse.exists():
#             return {'error': 'Invalid product or warehouse ID'}

#         available_stock = warehouse.get_stock_for_product(product)
#         return {'product_id': product.id, 'warehouse_id': warehouse.id, 'stock': available_stock}

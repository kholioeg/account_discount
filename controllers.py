# -*- coding: utf-8 -*-
from openerp import http

# class AccountDiscount(http.Controller):
#     @http.route('/account_discount/account_discount/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_discount/account_discount/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_discount.listing', {
#             'root': '/account_discount/account_discount',
#             'objects': http.request.env['account_discount.account_discount'].search([]),
#         })

#     @http.route('/account_discount/account_discount/objects/<model("account_discount.account_discount"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_discount.object', {
#             'object': obj
#         })
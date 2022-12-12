# -*- coding: utf-8 -*-
# from odoo import http


# class UltraShine(http.Controller):
#     @http.route('/ultra_shine/ultra_shine', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ultra_shine/ultra_shine/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ultra_shine.listing', {
#             'root': '/ultra_shine/ultra_shine',
#             'objects': http.request.env['ultra_shine.ultra_shine'].search([]),
#         })

#     @http.route('/ultra_shine/ultra_shine/objects/<model("ultra_shine.ultra_shine"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ultra_shine.object', {
#             'object': obj
#         })

# -*- coding: utf-8 -*-
# from odoo import http


# class TokoFarrel(http.Controller):
#     @http.route('/toko_farrel/toko_farrel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/toko_farrel/toko_farrel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('toko_farrel.listing', {
#             'root': '/toko_farrel/toko_farrel',
#             'objects': http.request.env['toko_farrel.toko_farrel'].search([]),
#         })

#     @http.route('/toko_farrel/toko_farrel/objects/<model("toko_farrel.toko_farrel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('toko_farrel.object', {
#             'object': obj
#         })

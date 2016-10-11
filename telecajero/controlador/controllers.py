# -*- coding: utf-8 -*-
from openerp import http

# class telecajero(http.Controller):
#     @http.route('/telecajero/telecajero/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/telecajero/telecajero/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('telecajero.listing', {
#             'root': '/telecajero/telecajero',
#             'objects': http.request.env['telecajero.telecajero'].search([]),
#         })

#     @http.route('/telecajero/telecajero/objects/<model("telecajero.telecajero"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('telecajero.object', {
#             'object': obj
#         })

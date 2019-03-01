# -*- coding: utf-8 -*-
from odoo import http

# class ExpeditorManagement(http.Controller):
#     @http.route('/expeditor_management/expeditor_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/expeditor_management/expeditor_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('expeditor_management.listing', {
#             'root': '/expeditor_management/expeditor_management',
#             'objects': http.request.env['expeditor_management.expeditor_management'].search([]),
#         })

# @http.route('/expeditor_management/expeditor_management/objects/<model(
# "expeditor_management.expeditor_management"):obj>/', auth='public') def object(self, obj, **kw): return
# http.request.render('expeditor_management.object', { 'object': obj })

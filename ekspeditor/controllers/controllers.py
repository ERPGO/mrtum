# -*- coding: utf-8 -*-
from odoo import http

# class Ekspeditor(http.Controller):
#     @http.route('/ekspeditor/ekspeditor/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ekspeditor/ekspeditor/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ekspeditor.listing', {
#             'root': '/ekspeditor/ekspeditor',
#             'objects': http.request.env['ekspeditor.ekspeditor'].search([]),
#         })

#     @http.route('/ekspeditor/ekspeditor/objects/<model("ekspeditor.ekspeditor"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ekspeditor.object', {
#             'object': obj
#         })
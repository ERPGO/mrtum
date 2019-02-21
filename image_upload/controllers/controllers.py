# -*- coding: utf-8 -*-
from odoo import http

# class ImageUpload(http.Controller):
#     @http.route('/image_upload/image_upload/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/image_upload/image_upload/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('image_upload.listing', {
#             'root': '/image_upload/image_upload',
#             'objects': http.request.env['image_upload.image_upload'].search([]),
#         })

#     @http.route('/image_upload/image_upload/objects/<model("image_upload.image_upload"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('image_upload.object', {
#             'object': obj
#         })
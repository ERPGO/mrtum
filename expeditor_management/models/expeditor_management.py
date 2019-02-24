# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class expeditor_management(models.Model):
    _name = "expeditor_management.expeditor_management"
    _description = "Expeditor Management"

    name = fields.Char(string="Name", default=datetime.today())
    order_id = fields.Many2one('sale.order', string="Sale Order")
    order_line = fields.One2many('sale.order.line', related='order_id.order_line')
    location_id = fields.Many2one(string="Customer Location", related='order_id.location_id')
    proof_image = fields.Binary(string="Proof Image")

    street = fields.Char(string="Street")
    map_location = fields.Html(string="Map location", compute="_get_map_url")

    @api.onchange('street')
    def _get_map_url( self ):
        streetname = self.street
        streetname_link = streetname.replace(" ", "+")
        link = '<p><a href="https://maps.google.com/maps?z=8&amp;q={streetname_link}+Azerbaijan" target="_blank">{' \
               'streetname}</a></p> '
        hyperlink = link.format(streetname_link=streetname_link, streetname=streetname)
        self.map_location = hyperlink

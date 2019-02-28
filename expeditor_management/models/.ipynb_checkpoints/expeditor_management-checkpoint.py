# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, date



class expeditor_assignments(models.Model):
    _name = "expeditor_assignment"
    _description = "Expeditor Management"
    
    name = fields.Char(string="Name", default="_get_assignment_name")

    def _get_assignment_name():
        current_date = datetime.now()
        current_month = current_date.strftime("%B")
        day_of_month = current_date.day
        current_year = current_date.year
        week_number = (day_of_month - 1) // 7 + 1
        print(str(current_year) + " " + current_month + " Week " + str(week_number))        
    
    user_id = fields.Many2one('res.users', string="Expeditor")
    request_ids = fields.One2many('expeditor_requests', 'assignment_id', string="Requests")
    
    
    
class expeditor_requests(models.Model):
    _name = "expeditor_requests"
    _description = "Expeditor Requests"

    name = fields.Char(string="Name", default=date.today())
    order_id = fields.Many2one('sale.order', string="Sale Order")
    order_line = fields.One2many('sale.order.line', related='order_id.order_line')
    location_id = fields.Many2one('stock.location',string="Customer Location")
    partner_id = fields.Many2one(string="Customer", related='location_id.partner_id')
    user_id = fields.Many2one('res.users', string="Expeditor")
    proof_image = fields.Binary(string="Proof Image")
    assignment_id = fields.Many2one('expeditor_assignment', string="Assignment")
    
    street = fields.Char(string="Street")
    map_location = fields.Html(string="Map location", compute="_get_map_url")

    @api.onchange('street')
    def _get_map_url( self ):
        if self.street:
            streetname = self.street
            streetname_link = streetname.replace(" ", "+")
            link = '<p><a href="https://maps.google.com/maps?z=8&amp;q={streetname_link}+Azerbaijan" target="_blank">{' \
               'streetname}</a></p> '
            hyperlink = link.format(streetname_link=streetname_link, streetname=streetname)
            self.map_location = hyperlink
            

class stock_expeditor(models.Model):
    _inherit = 'stock.location'
    
    user_id = fields.Many2one('res.users', string="Expeditor")
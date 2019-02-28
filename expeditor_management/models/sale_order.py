# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderExpeditor(models.Model):
    _inherit = 'sale.order'

    location_id = fields.Many2one(related="partner_id.property_stock_customer", string="Customer Location")
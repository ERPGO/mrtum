# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderExpeditor(models.Model):
    _inherit = 'sale.order'

    location_id = fields.Many2one('stock.location', string="Customer Location")
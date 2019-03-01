# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderExpeditor(models.Model):
    _inherit = 'res.users'

    is_expeditor = fields.Boolean(string="Is a Exspeditor", default=True)

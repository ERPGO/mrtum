# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Ekspeditor(models.Model):
    _inherit = 'crm.lead'
    
    testimage = fields.Many2many('ir.attachment', string="Image")
    testfield = fields.Char(string='testfield')


# class ekspeditor(models.Model):
#     _name = 'ekspeditor.ekspeditor'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
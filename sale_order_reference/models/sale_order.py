# Copyright 2020 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

#   Char, Float, Integer, Text
#   Many2one, Many2many, One2many
    order_reference = fields.Char(
        string="Custom Reference",
#       required=True,
#       readonly=True,
        track_visibility='always',
#                         onchange
#         compute='_compute_order_reference'
    )
    
    @api.constrains('order_reference')
    def _reference_constrains(self):
        for rec in self:
            if rec.order_reference == 'hello':
                raise ValidationError('Error')
                
#     def write(self, vals) 更新
#     vals = {
#        'order_reference': 'test'
#     }
#     def create(self, vals) 作成
#     def unlink(self, vals) 削除
    
#     def _compute_order_reference(self):
#         for order in self:
#             order.order_reference = order.partner_id.ref

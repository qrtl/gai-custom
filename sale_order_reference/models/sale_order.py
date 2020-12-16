# Copyright 2020 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

#   Char, Float, Integer, Text
#   Many2one, Many2many, One2many
    order_reference = fields.Char(
        string="Custom Reference",
#       required=True,
#       readonly=True,
#       track_visibility='always',
#       compute='_compute_order_reference'
    )
    
#     def _compute_order_reference(self):
#         for order in self:
#             order.order_reference = order.partner_id.ref

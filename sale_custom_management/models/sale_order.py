# Copyright 2020 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def test(self):
        # self: アクションがトリガーされたレコード
        # _(文字列): 翻訳対象項目
        order_name = self.name
        raise UserError(_("%s's Test Button is clicked" % order_name))

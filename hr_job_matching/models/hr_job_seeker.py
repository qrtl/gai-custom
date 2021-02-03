# Copyright 2021 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class JobSeeker(models.Model):
    _name = "hr.job.seeker"

    name = fields.Char(required=True)

# Copyright 2021 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class Job(models.Model):
    _inherit = "hr.job"

    job_seeker_ids = fields.Many2many(
        "hr.job.seeker",
        string="Job Seekers",
    )

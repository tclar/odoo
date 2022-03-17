from odoo import fields, models


class Company(models.Model):
    _inherit = "res.company"

    report_background_image = fields.Binary('Background Image')

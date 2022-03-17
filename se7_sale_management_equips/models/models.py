# -*- coding: utf-8 -*-

from odoo import models, fields, api


class se7_sale_management_equips(models.Model):
    _inherit = 'product.template'

    crear_equipo = fields.Boolean()

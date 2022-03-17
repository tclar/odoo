from odoo import models, fields, api


class ExtendedSaleOrder(models.Model):
    _inherit = 'sale.order'

    es_reparacion = fields.Boolean(index=True, track_visibility='onchange', string="Es una reparacion?")
    equipo_reparacion = fields.Many2one('sale_management_equips.equipo', index=True, track_visibility='onchange', string="Equipo a reparar")

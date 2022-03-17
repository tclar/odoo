# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ExtendedStockPicking(models.Model):
    _inherit = 'stock.picking'

    # reparaciones = fields.Many2many('reparacion','reparacions', string="Lista de reparaciones")


    @api.multi
    def button_validate(self):
        a = super(ExtendedStockPicking, self).button_validate()
        x = self
        self.create_equipos(x)
        return

    @api.model
    def create_equipos(self, vals):
        for stock in vals:
            for line in stock.move_line_ids:
                if line.product_id.crear_equipo:
                    a_crear = {
                        'name': line.product_id.display_name,
                        'num_serie': line.lot_id.display_name,
                        'product_reference': line.product_id.id,
                        'pedido_venta': stock.sale_id.id,
                        'user_reference': stock.partner_id.id
                    }
                    self.env['sale_management_equips.equipo'].create(a_crear)

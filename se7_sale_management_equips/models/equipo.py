# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Equipo(models.Model):
    _name = "sale_management_equips.equipo"
    _inherit = ['mail.thread', 'mail.mail', 'mail.activity.mixin']
    _rec_name = 'title'
    _sql_constraints = [('const_serie_product', 'UNIQUE(num_serie,product_reference)', 'El producto ya existe con este '
                                                                                       'numero de serie')]

    name = fields.Char(string="Nombre", index=True, track_visibility='onchange')
    num_serie = fields.Char(string="Num. serie", index=True, track_visibility='onchange')
    product_reference = fields.Many2one('product.product', 'Producto', index=True, track_visibility='onchange')
    pedido_venta = fields.Many2one('sale.order', readonly="True", index=True, track_visibility='onchange')
    user_reference = fields.Many2one('res.partner', string="Propietario", index=True, track_visibility='onchange')
    sale_equipos = fields.One2many('sale.order', 'equipo_reparacion',
                                   "Todas las sales que tienen este equipo a reparar")
    title = fields.Char(compute="calculate_title", store=True)

    puesta_en_marcha = fields.Date('Puesta en marcha')
    fecha_fin_garantia = fields.Date('Fecha fin garantía')

    imagenes_equipo = fields.One2many('sale_management_equips.imagen_equipo', 'equipo', 'Imagenes equipo')

    @api.depends('name', 'num_serie')
    def calculate_title(self):
        for x in self:
            x.title = x.name + "-" + x.num_serie

    @api.onchange('product_reference')
    def change_product(self):
        self.name = self.product_reference.name

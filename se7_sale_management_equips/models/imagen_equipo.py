from odoo import fields, models


class ImagenEquipo(models.Model):
    _name = 'sale_management_equips.imagen_equipo'
    _description = 'Imagenes del equipo'

    def compute_name(self):
        for imagen in self:
            imagen.name = '%s, %s' % (imagen.equipo.name, imagen.id)

    name = fields.Char('Nombre', compute=compute_name)
    equipo = fields.Many2one('sale_management_equips.equipo', 'Equipo')
    imagen = fields.Binary('Imagen')

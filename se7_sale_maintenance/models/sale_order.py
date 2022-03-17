import base64

from odoo import fields, models, api, modules, tools


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _get_default_image(self):
        image_path = modules.get_module_resource('se7_sale_maintenance', 'static/src/img', 'settings.png')
        return tools.image_resize_image_small(base64.b64encode(open(image_path, 'rb').read()))

    parte_de_trabajo = fields.Boolean(default=False)
    es_reparacion = fields.Boolean('Is Repair', compute='compute_tipo')
    es_mantenimiento = fields.Boolean('Is Maintenance', compute='compute_tipo')
    es_instalacion = fields.Boolean('Is Installation', default=True)
    tipo_trabajo = fields.Selection(
        [('repair', 'Repair'), ('mantinance', 'Maintenance'), ('installation', 'Installation')], 'Job Type',
        default='installation')
    image_small = fields.Binary(default=_get_default_image, readonly=True)

    @api.depends('tipo_trabajo')
    def compute_tipo(self):
        for order in self:
            order.es_reparacion = order.tipo_trabajo == 'repair'
            order.es_mantenimiento = order.tipo_trabajo == 'mantinance'

    @api.onchange('tipo_trabajo')
    def onchange_tipo_trabajo(self):
        param_name = False
        if self.tipo_trabajo == 'repair':
            param_name = 'repair_default_journal_id'
        elif self.tipo_trabajo == 'mantinance':
            param_name = 'mantinance_default_journal_id'
        if param_name:
            self.diario_facturacion = int(self.env['ir.config_parameter'].sudo().get_param(param_name)) or False
        else:
            self.diario_facturacion = False


class SaleReport(models.Model):
    _inherit = "sale.report"

    es_reparacion = fields.Boolean('Is Repair', related='order_id.es_reparacion')
    es_mantenimiento = fields.Boolean('Is Maintenance', related='order_id.es_mantenimiento')
    es_instalacion = fields.Boolean('Is Installation', related='order_id.es_instalacion')

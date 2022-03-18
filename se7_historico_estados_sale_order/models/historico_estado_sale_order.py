from odoo import fields, models, api


class HistoricoEstadoSaleOrder(models.Model):
    _name = 'sale.historico_estado_sale_order'

    name = fields.Char(compute='compute_name')
    sale_order = fields.Many2one('sale.order', ondelete='cascade')
    estado_anterior = fields.Char('Estado Anterior')
    estado_nuevo = fields.Char('Estado Nuevo')
    fecha = fields.Datetime('Fecha y hora del cambio')
    usuario = fields.Many2one('res.users')
    empleado = fields.Many2one('hr.employee')
    editor = fields.Char(compute='compute_editor')
    observaciones = fields.Text('Observaciones')

    @api.depends('sale_order', 'estado_nuevo', 'estado_anterior')
    def compute_name(self):
        for historico in self:
            historico.name = '%s, %s -> %s' % (
                historico.sale_order.name, historico.estado_anterior, historico.estado_nuevo
            )

    @api.depends('usuario.name', 'empleado.name')
    def compute_editor(self):
        for historico in self:
            if historico.usuario:
                historico.editor = historico.usuario.name
            elif historico.empleado:
                historico.editor = historico.empleado.name
            else:
                historico.editor = ''


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    historico_estado = fields.One2many('sale.historico_estado_sale_order', 'sale_order')

    @api.multi
    def write(self, values):
        if values.get('estado_trabajo') is not None:
            sale_order_id = self.id
            estado = values.get('estado_trabajo')
            label_estado = dict(self._fields['estado_trabajo'].selection).get(estado)
            estado_anterior = dict(self._fields['estado_trabajo'].selection).get(self.estado_trabajo)
            current_user = self.env.user.id
            if estado in ['enpausa', 'finalizado', 'en_proceso']:
                vals_list = {
                    'sale_order': sale_order_id,
                    'estado_anterior': estado_anterior,
                    'estado_nuevo': label_estado,
                    'fecha': fields.datetime.now(),
                    'usuario': current_user,
                }
                if values.get('empleado') is not None:
                    vals_list.update({
                        'empleado': values.get('empleado'),
                    })
                self.env['sale.historico_estado_sale_order'].create(vals_list)
        return super().write(values)

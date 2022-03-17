from odoo import fields, models, api


class SummaryDeliveriesByProductModal(models.TransientModel):
    _name = 'summary_deliveries_by_product.modal'

    name = fields.Char()
    day = fields.Date('Day', required=True, default=fields.Date.today())
    product_movments = fields.One2many('summary_deliveries_by_product.product_movment', 'modal',
                                       compute='compute_product_movments')

    @api.depends('day')
    def compute_product_movments(self):
        for summary in self:
            if not summary.day:
                return None
            stock_move_movments = self.env['stock.move.line'].search([
                ('state', '=', 'assigned'),
                ('date', '>=', summary.day.strftime("%Y-%m-%d 00:00:00")),
                ('date', '<=', summary.day.strftime("%Y-%m-%d 23:59:59")),
                ('picking_id.picking_type_id.code', '=', 'outgoing'),
            ])
            product_movments = {}
            for movment in stock_move_movments:
                key = movment.product_id.name
                if not product_movments.get(key):
                    product_movments.update({key: {
                        'product_name': key,
                        'product_qty': 0,
                    }})
                product_movments[key].update(
                    {'product_qty': product_movments[key]['product_qty'] + movment['product_qty']}
                )
            if product_movments:
                for mov in product_movments.values():
                    summary.product_movments = [(0, 0, mov)]


class ProductMovment(models.TransientModel):
    _name = 'summary_deliveries_by_product.product_movment'

    name = fields.Char()
    modal = fields.Many2one('summary_deliveries_by_product.modal')
    product_name = fields.Char('Product')
    product_qty = fields.Float('Real Reserved Quantity')

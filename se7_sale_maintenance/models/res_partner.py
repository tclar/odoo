from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    new_sale_order_count = fields.Integer(compute='_compute_new_sale_order_count', string='Sale Order Count')

    def _compute_new_sale_order_count(self):
        all_partners = self.with_context(active_test=False).search([('id', 'child_of', self.ids)])
        all_partners.read(['parent_id'])

        sale_order_groups = self.env['sale.order'].read_group(
            domain=[('es_instalacion', '=', False),
                    ('partner_id', 'in', all_partners.ids)],
            fields=['partner_id'], groupby=['partner_id']
        )
        for group in sale_order_groups:
            partner = self.browse(group['partner_id'][0])
            while partner:
                if partner in self:
                    partner.new_sale_order_count += group['partner_id_count']
                partner = partner.parent_id

    def _compute_sale_order_count(self):
        # retrieve all children partners and prefetch 'parent_id' on them
        all_partners = self.with_context(active_test=False).search([('id', 'child_of', self.ids)])
        all_partners.read(['parent_id'])

        sale_order_groups = self.env['sale.order'].read_group(
            domain=[('es_instalacion', '=', True),
                    ('partner_id', 'in', all_partners.ids)],
            fields=['partner_id'], groupby=['partner_id']
        )
        for group in sale_order_groups:
            partner = self.browse(group['partner_id'][0])
            while partner:
                if partner in self:
                    partner.sale_order_count += group['partner_id_count']
                partner = partner.parent_id

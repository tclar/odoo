from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    mantinance_default_journal_id = fields.Many2one('account.journal', string='Mantinance default journal')
    repair_default_journal_id = fields.Many2one('account.journal', string='Repair default journal')

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        mantinance_default_journal_id = self.env["ir.config_parameter"].get_param(
            "mantinance_default_journal_id", default=None)
        repair_default_journal_id = self.env["ir.config_parameter"].get_param(
            "repair_default_journal_id", default=None)
        res.update(mantinance_default_journal_id=int(mantinance_default_journal_id),
                   repair_default_journal_id=int(repair_default_journal_id))
        return res

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('mantinance_default_journal_id',
                                                         self.mantinance_default_journal_id.id)
        self.env['ir.config_parameter'].sudo().set_param('repair_default_journal_id', self.repair_default_journal_id.id)

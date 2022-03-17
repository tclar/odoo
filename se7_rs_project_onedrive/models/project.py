from odoo import fields, models


class Project(models.Model):
    _inherit = 'project.project'

    onedrive_link = fields.Char('Link OneDrive')


class Task(models.Model):
    _inherit = 'project.task'

    onedrive_link = fields.Char('Link OneDrive', related='project_id.onedrive_link')

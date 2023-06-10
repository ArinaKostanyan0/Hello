from odoo import models, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'
    _description = 'Custom Task'

    note = fields.Text(string="Arina's description")
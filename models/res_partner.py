from odoo import api, fields,models


class Partner(models.Model):
    _inherit = 'res.partner'

    is_customernya = fields.Boolean(string='Customer', default=False)
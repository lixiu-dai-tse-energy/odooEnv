from odoo import api, fields, models
class EstateType(models.Model):
    _name = 'Estate.Type'
    _description = 'Estate Type'

    name = fields.Char('Properties', default = "Unknown", required=True, translate=True)

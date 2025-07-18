from odoo import models, fields

class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'EState Property Type'

    _order ="sequence, name"

    sequence = fields.Integer("Sequence", default=1, help="use to order type")
    name = fields.Char('name', required=True, unique=True)
    property_ids = fields.One2many('estate.property', 'property_type_id', string='Property Types')

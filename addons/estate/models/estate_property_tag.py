from odoo import models, fields
class PropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Property Tag'
    order = 'name'

    name = fields.Char(string="name", required=True, unique=True)
    color = fields.Integer(string="color", default=0, help='choose a color(0-15)')
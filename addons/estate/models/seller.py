from odoo import models, fields
class seller(models.Model):
    _name = 'seller'
    _description = 'Seller'


    name = fields.Char("Name", required=True)

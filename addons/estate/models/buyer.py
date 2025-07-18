from odoo import models, fields
class Buyer(models.Model):
    _name = 'buyer'
    _description = 'Buyer'

    name= fields.Char("Name : ", required=True)

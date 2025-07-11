from odoo import models,fields

class TestModel(models.Model):
    _name="test_model"
    _description = "test model"
    #_order = "sequence"

    name = fields.Char('Properties', required=True, translate=True)
    description = fields.Char('Description', required=False)
    expected_price = fields.Float(string="Expected Price", required = True)
    postcode = fields.Char('Poste Code : ', required = True, translate = True)
    date_avaibility = fields.Date(string='Date avaibility : ', copy=False, default=fields.Date.today())
    selling_price = fields.Float('Selling price : ', required = False, readonly=True, copy=False)
    bedrooms = fields.Integer("Number of bedrooms : ", required = False,default = 2)
    living_area = fields.Integer('Living area : ')
    facades = fields.Integer('Living area : ')
    garage = fields.Integer('Number of garage : ')
    garden = fields.Boolean("Is there a garden ? ")
    garden_area = fields.Integer("Garden area : ")
    active = fields.Boolean("Is there a active ? ", default = False, active=False)
    state = fields.Selection([("New", "New"), ("Offer Received", "Offer Received"), ("Offer accepted", "Offer accepted"),("Sold", "Sold"),("Cancelled", "Cancelled")], copy=False, required=True, default=("New"))
    garden_orientation = fields.Selection( [("south","south"), ("north","north"), ("west","west"), ("east","east")])



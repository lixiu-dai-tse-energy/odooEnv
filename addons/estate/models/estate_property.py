from email.policy import default


from odoo import models,fields, api
from odoo.exceptions import ValidationError, UserError


class EstateModel(models.Model):
    _name="estate.property"
    _description = "estate property"
    _order = "id desc"
    #_order = "sequence"
    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0)', 'Expected price must be strictly positive'),
        ('check_selling_price', 'CHECK(selling_price >= 0)', 'Selling price must be positive'),
    ]
    name = fields.Char('Properties', default = "Unknown", required=True, translate=True)
    last_seen = fields.Datetime('Last Seen', default =fields.Datetime.now())
    description = fields.Char('Description', required=False)
    expected_price = fields.Float(string="Expected Price", required = True)
    postcode = fields.Char('Poste Code : ', required = True, translate = True)
    date_avaibility = fields.Date(string='Date avaibility : ', copy=False, default=fields.Date.today())
    selling_price = fields.Float('Selling price : ', required = False, readonly=True, copy=False)
    bedrooms = fields.Integer("Number of bedrooms : ", required = False,default = 2)
    living_area = fields.Integer('Living area : ',  required = False)
    facades = fields.Integer('facedes : ')
    garage = fields.Integer('Number of garage : ')
    garden = fields.Boolean("Is there a garden ? ")
    garden_area = fields.Integer("Garden area : ")
    active = fields.Boolean("Is there a active ? ", default = True, active=False)
    state = fields.Selection([("New", "New"), ("Offer Received", "Offer Received"), ("Offer accepted", "Offer accepted"),("Sold", "Sold"),("Cancelled", "Cancelled")],widget="statusbar", statusbar_visible="New, Offer Received,Offer Accepted, Sold, Canncelled",copy=False, required=True, default="New")
    garden_orientation = fields.Selection( [("south","south"), ("north","north"), ("west","west"), ("east","east")])

    property_type_id=fields.Many2one('estate.property.type','Property Type', )
    property_seller_id=fields.Many2one('seller', 'Salesman' )
    property_buyer_id=fields.Many2one('buyer', 'Property buyer')
    property_tag_ids = fields.Many2many('estate.property.tag', 'property_id', string=' ', )
    property_offer_ids = fields.One2many('estate.property.offer','property_id', ' ')
    total_area=fields.Float("Total Area", compute="_compute_total_area", store=True, readonly=True, copy=False)
    best_price = fields.Float("Best Price", compute="_compute_best_price", store=True, readonly=True, copy=False)
    @api.depends('property_offer_ids.price')
    def _compute_best_price(self):
        for property in self:
            if(property.property_offer_ids):
             property.best_price = max(property.property_offer_ids.mapped('price'))
            else:
                property.best_price =0.0

    @api.depends('living_area','garden_area' )
    def _compute_total_area(self):
        for property in self:
            property.total_area = self.living_area+self.garden_area

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = 0
            self.garden_orientation = ""

    def action_canncel(self):
        for property in self:
            if property.state!="Sold":
                property.state="Cancelled"
            else:
                raise UserError('the property is sold')
        return True
    def action_sold(self):
        for property in self:
            if property.state != "Cancelled":
                property.state="Sold"
            else:
                raise UserError('the property is cancelled')

        return True


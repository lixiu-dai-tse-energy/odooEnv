from datetime import timedelta

from reportlab.platypus.tableofcontents import delta

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools import float_compare, float_is_zero


class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Property Offer'
    _order ="price desc"
    _sql_constraints = [
        ('check_offer_price', 'CHECK(price > 0)', 'Offer price must be strictly positive'),
    ]
    # name = fields.Char('Property offer ', required = False, copy=False)
    # price_partner = fields.Float('Price partner ', required = False, copy=False)
    status=fields.Selection([("Accepted","Accepted"), ("Refused", "Refused")])
    price = fields.Float('Price ', required = False, copy=False)
    partner_id=fields.Many2one('res.partner', 'Partner ', required = True)
    property_id = fields.Many2one('estate.property', 'Property offer', ondelete='cascade', required=True)
    validity = fields.Integer('Validity', required=False, default=7)
    date_deadline = fields.Date("Deadline", compute="compute_deadline", inverse="_inverse_deadline", store=True,  )
    date_created = fields.Date('Created', required=False, default=fields.Date.today())
    @api.depends('validity', 'date_created')
    def compute_deadline(self):
        for propertyOffer in self:
            if propertyOffer.date_created:
                propertyOffer.date_deadline = propertyOffer.date_created +timedelta(propertyOffer.validity)
            else:
                propertyOffer.date_deadline = fields.Date.today() + timedelta(propertyOffer.validity)

    def _inverse_deadline(self):
        for propertyOffer in self:
            if propertyOffer.date_created:
                delta = propertyOffer.date_deadline - propertyOffer.date_created
                propertyOffer.validity = delta.days
            else:
                delta = propertyOffer.date_deadline - fields.Date.today()
                propertyOffer.validity = delta.days
    def action_accept_offer(self):
        for offer in self:
            offer.status = "Accepted"
            if offer.property_id.selling_price== 0:
                offer.property_id.selling_price=offer.price
            else:
                raise UserError("there is another offer accepted")
        return True
    def action_refuse_offer(self):
        for offer in self:
            offer.status = "Refused"
        return True
    @api.constrains('price')
    def _check_price(self):
        for offer in self:
            if  not float_is_zero(offer.price,precision_digits=2) and float_compare(offer.price, offer.property_id.expected_price*0.9,precision_digits=2)<0:
                raise UserError("The selling price must be at least 90% of the expected price, you must reduce the expected price if you want to accept the offer")
        return True
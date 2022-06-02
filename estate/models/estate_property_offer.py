from odoo import models, fields


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "This is the description for the estate property offer table."

    price = fields.Float('Price')
    status = fields.Selection(
        string = 'Status',  # string is the label of the field seen by the user
        selection = [('accepted', 'Accepted'), ('refused', 'Refused')])
    partner_id = fields.Many2one("rest.partner", string = 'Partner', required = True)
    property_id = fields.Many2one('estate.property', string = 'Property', required = True)

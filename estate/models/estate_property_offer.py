from odoo import models, fields, api


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "This is the description for the estate property offer table."

    price = fields.Float('Price')
    status = fields.Selection(
        string = 'Status',  # string is the label of the field seen by the user
        selection = [('accepted', 'Accepted'), ('refused', 'Refused')])
    partner_id = fields.Many2one("res.partner", string = 'Partner', required = True)
    property_id = fields.Many2one('estate.property', string = 'Property', required = True, invisible=True)

    # Chapter 9: compute and inverse
    validity = fields.Integer("Validity (days)", default = 7)
    date_deadline = fields.Date("Deadline", compute = "_compute_date_deadline", inverse = "_inverse_date_deadline")

    # Functions to compute field values
    @api.depends("validity")
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = fields.Date.add(fields.Date.today(), days = record.validity)
    
    def _inverse_date_deadline(self):
        for record in self:
            delta = record.date_deadline - fields.Date.today()
            record.validty = delta.days
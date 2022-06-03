from odoo import models, fields, api, tools
from odoo.exceptions import UserError, AccessError


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "This is the description for the estate property."

    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Date Availability', copy=False, default=lambda self: fields.Date.add(fields.Date.today(), months=3))
    expected_price = fields.Float('Expected Price', required=True)
    selling_price = fields.Float('Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer('Number Bedrooms', default=2)
    living_area = fields.Integer('Living Area')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection(
        string='Garden Orientation',  # string is the label of the field seen by the user
        selection=[('north', 'North'), ('east', 'East'), ('south', 'South'), ('west', 'West')])
    state = fields.Selection(
        string = 'State', 
        selection = [('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'), ('canceled', 'Canceled')],
        required = True, 
        copy = False, 
        default = 'new'
    )
    
    # computed fields
    total_area = fields.Float(compute = "_compute_total_area")
    best_offer = fields.Float(compute = "_compute_best_price")
    
    # reserved fields
    active = fields.Boolean('Active', default=True)

    # many2one fields (Chapter 8)
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    ## buyer (res.partner)
    buyer = fields.Many2one("res.partner", string="Buyer", copy=False)
    ## salesperson (res.user)
    salesperson = fields.Many2one("res.users", string="Salesperson", default=lambda self: self.env.user)

    # many2many fields (Chapter 8)
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")

    # one2many fields (Chapter 8)
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")

    # Chapter 9: computing functions
    @api.depends("garden_area", "living_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area

    @api.depends("offer_ids")
    def _compute_best_price(self):
        # this could be optimised
        # for record in self:
        #     max = -1
        #     for offer in record.offer_ids:
        #         if max < offer.price:
        #             max = offer.price
        # record.best_offer = max
        for record in self:
            offers = map(lambda offer: record.price, record.offer_ids)
            record.best_offer = max(offers)
        

    # Chapter 9: onchange computing functions
    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = 0
            self.garden_orientation = False

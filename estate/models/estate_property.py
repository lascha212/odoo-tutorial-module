from odoo import models, fields


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "This is the description for the estate property."

    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Date Availability', copy=False, default=lambda self: fields.Date.sum(fields.Date.today(), months=+1))
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

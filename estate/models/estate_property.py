from odoo import models, fields


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "This is the description for the estate property."

    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Date Availability')
    expected_price = fields.Float('Expected Price', required=True)
    selling_price = fields.Float('Selling Price')
    bedrooms = fields.Integer('Number Bedrooms')
    living_area = fields.Integer('Living Area')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection(
        string='Type',  # string is the label of the field seen by the user
        selection=[('north', 'North'), ('east', 'East'), ('south', 'South'), ('west', 'West')])

from odoo import models, fields


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "This is the description of the estate property tag model."

    name = fields.Char('Name', required=True)    
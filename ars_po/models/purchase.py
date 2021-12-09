from odoo import fields, models
from odoo.exceptions import ValidationError


class Purchase(models.Model):
    _inherit = "purchase.order"

    catatan = fields.Char(string="Catatan")
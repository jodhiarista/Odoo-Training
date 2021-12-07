from odoo import fields, models

class CatatanCRM(models.Model):
    _inherit = "crm.lead"

    catatan = fields.Char(string="Catatan")
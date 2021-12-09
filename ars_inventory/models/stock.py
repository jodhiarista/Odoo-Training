from odoo import fields, models

class StockModule(models.Model):
    _inherit = 'stock.picking'
    
    keterangan = fields.Char(
        string = 'Keterangan'
    )
    
    
    
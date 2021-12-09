# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class SaleTTUMS(models.Model):
    _name = "sale.ttums"

    name = fields.Char("catatan", required=True)
    
    


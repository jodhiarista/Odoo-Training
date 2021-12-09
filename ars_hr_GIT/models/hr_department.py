# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Department(models.Model):
    _inherit = 'hr.department'

    catatan = fields.Char(string='Lalala')

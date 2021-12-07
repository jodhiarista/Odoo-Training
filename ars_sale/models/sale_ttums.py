# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class SaleTTUMS(models.Model):
    _name = "sale.ttums"

    name = fields.Char("Nomor", states={'draft': [('readonly', False)]}, readonly=True)
    partner_id = fields.Many2one('res.partner', string="Customer", states={'draft': [('readonly', False)]}, readonly=True)
    date_ttums = fields.Datetime(string="Date", states={'draft': [('readonly', False)]}, readonly=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirm'),
        ('sale', 'Sales Order'),
        ], string='Status', readonly=True, copy=False, default='draft')
    ttums_line_ids = fields.One2many('sale.ttums.line', 'ttums_id', string="TTUMS Line", states={'draft': [('readonly', False)]}, readonly=True)
    sale_order_id = fields.Many2one('sale.order', string="Sale Order", readonly=True)

    def confirm_ttums(self):
        self.state = 'confirmed'
    
    def cancel_ttums(self):
        self.state = 'draft'
    
    def create_so(self):
        so = self.env['sale.order'].create({
            "partner_id": self.partner_id.id,
            "date_order": self.date_ttums
        })
        
        for line in self.ttums_line_ids:
            so_line = self.env['sale.order.line'].create({
                "product_id": line.product_id.id,
                "name": line.product_id.name,
                "product_uom_qty": line.quantity,
                "price_unit": line.price,
                "order_id": so.id,
            })
        self.state = 'sale'
        self.sale_order_id = so.id
        return so
    
class SaleTTUMSLine(models.Model):
    _name = "sale.ttums.line"

    ttums_id = fields.Many2one('sale.ttums')
    product_id = fields.Many2one('product.product', string="Product")
    price = fields.Float(string="Harga")
    quantity = fields.Float(string="Jumlah")


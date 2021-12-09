# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Inherit Stock Inventory',
    'category': 'Hidden',
    'version': '1.0',
    'summary': 'Penambahan Field Ke Inventory',
    'description':
        """
======================== ****
INVENTORY FOR ARISTA GROUP    ****
======================== ****
        """,
    'depends': ['stock'],
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/sale_ttums_views.xml',
        # 'views/hr_skill_views.xml'
        'views/stock_picking.xml'
        ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
}

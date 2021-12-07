# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Inherit Sale',
    'category': 'Hidden',
    'version': '1.0',
    'summary': 'Penambahan Field ke Sale',
    'description':
        """
======================== ****
Sale FOR ARISTA GROUP    ****
======================== ****
        """,
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_ttums_views.xml',
        # 'views/hr_skill_views.xml'
        ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
}

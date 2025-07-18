# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "Lixiu",
    'category': 'Category',
    'application': True,
    'description': """
        Description text
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
        'views/estate_property_form.xml',
    ],
    'demo': [
        'data/estate_property_domo.xml',
    ],
}
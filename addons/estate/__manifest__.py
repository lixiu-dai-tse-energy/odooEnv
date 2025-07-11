# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{ 'name': "Estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "Lixiu",
    'category': 'Category',
    'application': True,
    'description': """
    Description text
    """,
    # data files always loaded at installation
    #'data': [
   #     'views/mymodule_view.xml',
    #],
    # data files containing optionally loaded demonstration data
   # 'demo': [
       # 'demo/demo_data.xml',
  #  ],
  'data':
      [
'security/ir.model.access.csv',
'views/estate_property_views.xml',
'views/estate_menus.xml',
  ],
'demo': [
        'data/estate_property_domo.xml',
    ],

}
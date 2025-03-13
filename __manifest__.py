# -*- coding: utf-8 -*-
{
    'name': "Real Estate Advertisement module",

    'summary': "Manage and display real estate advertisements, with features such as offers and property details.",

    'description': """
Manage and display real estate advertisements, with features such as offers and property details.""",

    'author': "FRecaldeDev",
    'website': "https://www.odoo.com/page/crm",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Real Estate',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    
}


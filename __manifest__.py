{
    'name': "Real Estate Advertisement module",
    'summary': "Manage and display real estate advertisements, with features such as offers and property details.",
    'description': """
Manage and display real estate advertisements, with features such as offers and property details.""",
    'author': "FRecaldeDev",
    'website': "https://www.odoo.com/page/crm",

    'category': 'Real Estate',
    'version': '1.0',

    'depends': ['base', 'crm'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/real_estate_property_views.xml',  
    ],
    'installable': True,
    'application': True,
}

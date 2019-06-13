# -*- coding: utf-8 -*-
{
    'name': "sale_order_show_opportunity_id",

    'summary': """
Always shows oppportunity_id field in the 'other info' tab in sale order (instead of having to activate debug mode)
""",

    'description': """
Always shows oppportunity_id field in the 'other info' tab in sale order (instead of having to activate debug mode)
    """,

    'author': "Auneor Conseil",
    'website': "http://www.auneor-conseil.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}

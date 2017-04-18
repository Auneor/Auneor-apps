# -*- coding: utf-8 -*-
{
    'name': "pos_report_join_categories",

    'summary': """
    This Module display, when analyzing sale from point of sale,  categories, and subcategories
        """,

    'description': """
    This Module display, when analyzing sale from point of sale,  categories, and subcategories
    """,

    'author': "Auneor Conseil",
    'website': "http://www.auneor-conseil.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'pos_order.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
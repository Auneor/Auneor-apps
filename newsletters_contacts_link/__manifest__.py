# -*- coding: utf-8 -*-
{
    'name': "newsletters_contacts_link",

    'summary': """
        This module links contacts to newsletters
        """,

    'description': """
        This module links contacts to newsletters
    """,

    'author': "Auneor Conseil",
    'website': "http://www.auneor-conseil.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mass_mailing'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
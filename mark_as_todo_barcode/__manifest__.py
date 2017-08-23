# -*- coding: utf-8 -*-
{
    'name': "mark_as_todo_barcode",

    'summary': """
    This module add the capability when scanning a barcode O-BTN-mark-as-todo to 
    excecute this action inside a stock picking
        """,

    'description': """
    This module add the capability when scanning a barcode O-BTN-mark-as-todo to 
    excecute this action inside a stock picking
    """,

    'author': "Auneor Conseil",
    'website': "http://www.auneor-conseil.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
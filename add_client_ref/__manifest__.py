# -*- coding: utf-8 -*-
{
    'name': "add_client_ref",

    'summary': """
        This module add the client reference in quotation tree view and the purchase order tree view""",

    'description': """
        This module add the client reference in quotation tree view and the purchase order tree view
    """,

    'author': "Auneor Conseil",
    'website': "http://www.auneor-conseil.fr",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['sale'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_views.xml',
    ],
}
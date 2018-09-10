# -*- coding: utf-8 -*-
{
    'name': "sale_order_only_company_adress",

    'summary': """
        Module Auneor Conseil
        """,

    'description': """
        This module allows you to filter the customer list, the billing and delivery address in sales order forms.\n
        
        Customer list: Displays only customers whose type is society.\n
        List billing address and delivery : Displays only the addresses which are of type society.
         
    """,

    'author': "Auneor Conseil",
    'website': "http://www.auneor-conseil.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'views/sale_order.xml',

    ],
    # # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}

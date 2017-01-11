# -*- coding: utf-8 -*-
{
    'name': "view_events_from_partners",

    'summary': """
        This module shows the event associated to partner inside the partner view
        """,

    'description': """
        This module shows the event associated to partner inside the partner view
    """,

    'author': "Auneor Conseil",
    'website': "http://www.auneor-conseil.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Events',
    'version': '0.1',
    'images': ['static/image.png'],

    'depends': ['event'],

    'data': [
        'views/views.xml',
    ],
}
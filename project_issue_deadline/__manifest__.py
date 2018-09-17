# -*- coding: utf-8 -*-
{
    'name': "project_issue_deadline",

    'summary': """
    Add a deadline on project issue with two filters, one for late issues, and one for next 5 days issue""",

    'description': """
    Add a deadline on project issue with two filters, one for late issues, and one for next 5 days issue
    It add this deadline in portal as well
    """,

    'author': "Aunéor Conseil",
    'website': "http://www.auneor-conseil.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website_project_issue'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/project_issue.xml',
        "views/portal_template.xml",
        'views/cron.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
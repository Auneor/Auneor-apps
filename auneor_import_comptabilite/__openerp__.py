# -*- coding: utf-8 -*-
{
    'name': "auneor_import_comptabilite",

    'summary': """
        Un petit module pour importer des ecritures comptables
       """,

    'description': """
        Un petit module pour importer des ecritures comptables
        Ce module importe des fichiers CSV (Comma Separated Value)
        Les champs doivents êtres séparés par une virgule
        Le delimiteur de chaine est le guillemet anglais
        Les colonnes prises en compte sont:
        DATE	JAL	COMPTE	PCE	LIBELLE	DEBIT	CREDIT

    """,

    'author': "Auneor Conseil",
    'website': "http://www.auneor-conseil.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
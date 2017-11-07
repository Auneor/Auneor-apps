# -*- coding: utf-8 -*-
{
    'name': "Payment term decade",

    'summary': """
    Ce module permet de gerer les conditions de réglements à 30 jours decade
        """,

    'description': """
    Ce module permet de gerer les conditions de reglements decade
    Par exemple pour une facture au 1er novembre elle sera dûe le 10 décembre
    pour une facture au 15 novembre, elle sera dûe le 20 décembre
    """,

    'author': "Auneor Conseil",
    'website': "http://www.auneor-conseil.fr",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}

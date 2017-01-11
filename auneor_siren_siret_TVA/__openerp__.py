# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name' : 'siren siret TVA',
    'version' : '6.0.1',
    'author' : 'Auneor Conseil',
    'website': 'www.auneor-conseil.fr',
    'category' : 'Auneor/General',
    'license': 'AGPL-3',
    'description':'''
We add some enhances to OpenERP for France:
Add the SIRET/SIREN and RCS informations to partner.
        ''',
    'depends' : [
        'base',
    ],
    'demo' : [],
    'data' : [
        'base/res/partner/view/partner_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
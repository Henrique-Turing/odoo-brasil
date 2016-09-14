# -*- coding: utf-8 -*-
# © 2009  Renato Lima - Akretion
# © 2016 Danimar Ribeiro, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Brazilian Localization Sale',
    'description': 'Brazilian Localization for Sale',
    'category': 'Localisation',
    'license': 'AGPL-3',
    'author': 'Akretion, OpenERP Brasil',
    'website': 'http://openerpbrasil.org',
    'version': '10.0.1.0.0',
    'depends': [
        'sale', 'br_account',
    ],
    'data': [
        'views/br_base.xml',
        'views/sale_view.xml',
        'security/ir.model.access.csv',
        'security/l10n_br_sale_security.xml',
    ],
    'installable': True,
    'auto_install': False
}

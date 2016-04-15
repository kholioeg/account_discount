# -*- coding: utf-8 -*-
{
    'name': "Account Discount",

    'summary': """
        Apply Discount model to taxes""",

    'description': """
        The purpose is to apply discount record for the same tax model
    """,

    'author': "Khaled Hamed",
    'website': "http://www.grandtk.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'account_discount_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
    'installable': True,
}
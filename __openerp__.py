# -*- coding: utf-8 -*-
{
    'name': "Account Discount",

    'summary': """
        Use Tax model for discounts as well""",

    'description': """
        
        Odoo OpenERP Account Discount from Tax
    
This module adds new concept to use tax model as discount model and print both taxes and discounts separetly.

The steps to perform are very easy:

    First you define new tax with negative amount (e.g Name: Discount 10%, Amount: -0.10).
    Enable Is Discount Checkbox.
    Then add this dicount from the Taxes/Discounts column per invoice line.

This way, you can separate and analyze discounts using different account/analytic account as well.
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
        'account_discount_view.xml'
    ],
    'installable': True,
    'price': 5,
    'currency': 'EUR',
}

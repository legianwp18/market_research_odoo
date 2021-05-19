# -*- coding: utf-8 -*-
{
    'name': "Market Research",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Legian Wahyu P",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts','sale','crm'],

    # always loaded
    'data': [
        'data/ir.module.category.csv',
        'data/res.groups.xml',
        'security/ir.model.access.csv',
        'views/market.xml',
        'views/monitoring.xml',
        'views/academy.xml',
        'views/brand_view.xml',
        'views/printer_view.xml',
        'views/catridge_view.xml',
        'views/cat_customer.xml',
        'views/metode_pembelian.xml',
        'views/menu.xml',
    ],
}
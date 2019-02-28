# -*- coding: utf-8 -*-
{
    'name': "Expeditor Management",

    'summary': """
        Expeditor management module""",

    'description': """
        Expeditor management module
    """,

    'author': "ERPGO",
    'website': "http://www.erpgo.az",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'sale_management',
                'stock',
                'stock_account',
                'sale_stock'
                ],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/expeditor_management.xml',
        'views/sale_order.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}

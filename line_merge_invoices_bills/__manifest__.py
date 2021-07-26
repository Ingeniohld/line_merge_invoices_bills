# -*- coding: utf-8 -*-
{
    'name': 'Automatic Merge for Customer Invoice & Vendor Bill Lines',
    'summary': "Automatic Merge Customer Invoice & Vendor Bill Lines",
    'description': "Automatic Merge for Customer Invoice & Vendor Bill Lines for the same products",

    'author': 'Ingenio',
    'support': 'ba@ingeniohld.com',

    'category': 'Accounting',
    'version': '14.0.0.1.1',
    'depends': ['account'],

    'data': [
        'views/res_config_settings_views.xml',
    ],

    'license': "OPL-1",
    'price': 7,
    'currency': "EUR",

    'auto_install': False,
    'installable': True,

    'images': ['static/description/banner.png'],
    'pre_init_hook': 'pre_init_check',
}

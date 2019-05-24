# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Mail Outbound Static',
    'summary': 'Allows you to configure the from header for a mail server.',
    'version': '10.0.1.0.1',
    'category': 'Discuss',
    'website': 'https://laslabs.com/',
    'author': 'LasLabs, Odoo Community Association (OCA)',
    'license': 'LGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'base',
    ],
    'data': [
        'views/ir_mail_server_view.xml',
    ],
}
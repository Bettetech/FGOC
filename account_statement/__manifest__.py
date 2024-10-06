# -*- coding: utf-8 -*-


{
    'name': 'Customer statement of account reports in Odoo ',
    'category': 'Accounting',
    'version': '14.0.0.3',
    'summary': 'Apps for print customer statement report',
    'description': "",
    'author': 'Odox',
    'website': '',
    'images': [],
    'depends': ['base', 'account'],
    
    'data': ['security/ir.model.access.csv',
             'views/report.xml',
             'views/customer_statement_report.xml',
             'views/res_partner_view.xml',
             ],
    'installable': True,
    'price': 36,
    'currency': "EUR",
    'auto_install': False,
    'application': True,
    "images":["static/description/Banner.png"],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

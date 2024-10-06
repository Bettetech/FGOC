{
    ###(SACEP - Mounir Hashisho)###
    'name': 'Einvoice technical (FGOC)',
    'version': '14.0.1.0.0',
    'author': 'Odox SoftHub',

    'website': 'http://www.odoxsofthub.com',
    'license': 'GPL-3',
    'category': 'Accounting',
    'depends': ['base', 'base_accounting_kit'],

    'summary': 'Technical',
    'data': ['security/security.xml',
             'views/customer_inherit_view.xml',
             'views/product_template_inherited.xml',
             ],
    'installable': True,
    'auto_install': False,
}

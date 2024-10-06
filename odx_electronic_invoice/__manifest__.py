{
    ### (FGOC) ###
    'name': 'Electronic Invoice (FGOC)',
    'summary': """Electronic Invoicing with QR code and arabic translations.Vendor Bill, Customer Invoice and
        Vendor Credit Note Report with Arabic headers""",
    'version': '14.0.2.0',
    'author': 'Odox SoftHub',
    'website': 'https://www.odoxsofthub.com',
    'category': 'Invoicing',
    'description': """Electronic Invoicing with QR code and arabic translations,Separate fields for arabic address for partners,
        KSA Invoices,
        KSA format invoices
        Arabic Invoice,
        Customer Invoice,
        TX
        odx modules,
        ODOX,
        E-invoice,
        Vendor Credit Note Report
    """,
    'depends': ['base', 'account', 'l10n_sa_invoice', 'web'],
    'external_dependencies': {'python': ['qrcode']},
    'images': ['static/description/thumbnail.gif'],
    'license': 'OPL-1',
    "price": 14.98,
    "currency": "USD",

    'support': 'support@odoxsofthub.com',
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'report/invoice_report.xml',
        'report/report_template_tax.xml',
        'report/invoice_layout_tax.xml',
        'report/local_report_template.xml',
        'report/local_invoice_layout.xml',
        # 'report/invoice_portal_template.xml',
        'views/mail_template.xml',
        'views/res_company.xml',
        'views/res_partner.xml',
        'views/res_bank_view.xml',
        'views/product_arabic.xml',
        'views/account_account_view.xml',
        'views/linkestatic.xml',
        'views/qr_code_invoice_view.xml',
        'views/product_template_views.xml',
        'views/account_move_view.xml',

    ],
    'installable': True,
    'auto_install': False,
}

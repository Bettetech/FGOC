# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import math
import re
import time
import traceback

from odoo import api, fields, models, tools, _

_logger = logging.getLogger(__name__)

try:
    from num2words import num2words
except ImportError:
    _logger.warning("The num2words python library is not installed, amount-to-text features won't be fully available.")
    num2words = None

CURRENCY_DISPLAY_PATTERN = re.compile(r'(\w+)\s*(?:\((.*)\))?')


class ResCompany(models.Model):
    _inherit = 'res.company'

    arabic_name = fields.Char(string='Arabic Name')
    street_1_arabic = fields.Char(string='Street Arabic')
    street_2_arabic = fields.Char(string='Street2 Arabic')
    city_arabic = fields.Char(string='City Arabic')
    state_arabic = fields.Char(string='State Arabic')
    country_arabic = fields.Char(string='Country Arabic')
    phone_arabic = fields.Char(string='Phone')
    cr_number = fields.Char(string='CR No.')
    cc_number = fields.Char(string='CC No.')
    unit_no = fields.Char(string='Unit No')
    additional_no = fields.Char(string='Additional No')
    bank_id = fields.Many2one('res.bank', string='Bank')
    bank_city = fields.Char(string='City')
    vendor_no = fields.Char(string='Vendor No')
    iban_no = fields.Char(string='IBAN')
    swift_code = fields.Char(string='SWIFT Code')
    acc_num = fields.Char(string='Account Number')
    vat_arabic = fields.Char(string='Tax ID Arabic')


class TccResCurrency(models.Model):

    _inherit = 'res.currency'
    # @api.multi
    def amount_to_text(self, amount):
        print('jyfuytfiu')
        self.ensure_one()
        def _num2words(number, lang):
            try:
                return num2words(number, lang=lang).title()
            except NotImplementedError:
                return num2words(number, lang='en').title()
        if num2words is None:
            logging.getLogger('_name_').warning("The library 'num2words' is missing, cannot render textual amounts.")
            return ""
        formatted = "%.{0}f".format(self.decimal_places) % amount
        parts = formatted.partition('.')
        integer_value = int(parts[0])
        fractional_value = int(parts[2] or 0)
        lang_code = self.env.context.get('lang') or self.env.user.lang
        lang = self.env['res.lang'].with_context(active_test=False).search([('code', '=', lang_code)])
        if lang_code == 'ar_001':
            amount_words = tools.ustr('{amt_value} {amt_word}').format(
                amt_value=_num2words(integer_value, lang=lang.iso_code),
                amt_word='ريال',
            )
            if not self.is_zero(amount - integer_value):
                amount_words += ' ' + _('و') + tools.ustr(' {amt_value} {amt_word}').format(
                    amt_value=_num2words(fractional_value, lang=lang.iso_code),
                    amt_word='هللة',
                )
        else:
            amount_words = tools.ustr('{amt_value} {amt_word}').format(
                amt_value=_num2words(integer_value, lang=lang.iso_code),
                amt_word=self.currency_unit_label,
            )
            if not self.is_zero(amount - integer_value):
                amount_words += ' ' + _('and') + tools.ustr(' {amt_value} {amt_word}').format(
                    amt_value=_num2words(fractional_value, lang=lang.iso_code),
                    amt_word=self.currency_subunit_label,
                )
        return amount_words
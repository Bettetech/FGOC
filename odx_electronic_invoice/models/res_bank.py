# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResBank(models.Model):
    _inherit = 'res.bank'

    iban_no = fields.Char(string='Iban No')
    arabic_name = fields.Char(string='Arabic Name')
    street_1_arabic = fields.Char(string='Street Arabic')
    street_2_arabic = fields.Char(string='Street2 Arabic')
    city_arabic = fields.Char(string='City Arabic')
    state_arabic = fields.Char(string='State Arabic')

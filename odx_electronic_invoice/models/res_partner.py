# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    arabic_name = fields.Char(string='Arabic Name')
    street_1_arabic = fields.Char(string='Street')
    street_2_arabic = fields.Char(string='Street')
    city_arabic = fields.Char(string='Street')
    state_arabic = fields.Char(string='State')
    country_arabic = fields.Char(string='Country')
    phone_arabic = fields.Char(string='Phone')
    code = fields.Char(string='Code')
    cr_num = fields.Char(string='CR Number')
    cr_num_arabic = fields.Char(string='CR NO. Arabic')
    ref_arabic = fields.Char(string='Reference Arabic')
    vat_arabic = fields.Char(string='Tax ID Arabic')

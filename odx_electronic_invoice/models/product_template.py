from odoo import fields, models


class ProductInherit(models.Model):
    _inherit = 'product.template'

    hs_code = fields.Char(string='HS Code')

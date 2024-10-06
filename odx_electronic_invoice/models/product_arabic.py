from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    arabic_name = fields.Char(string='Arabic Name')

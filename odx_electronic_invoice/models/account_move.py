from odoo import api, fields, models, _
from odoo.http import request
from odoo.tools import html2plaintext


class AccountMove(models.Model):
    _inherit = 'account.move'

    project = fields.Char(string="Project")
    sc_num = fields.Char(string="SC Number")
    gross_weight = fields.Float(string="Total Gross Weight")
    net_weight = fields.Float(string="Total Net Weight")
    pallets_num = fields.Float(string="No. of Pallets")
    contact_id = fields.Many2one('res.partner', string='Attention/Contact')
    contact = fields.Many2one('res.partner', string='Attention/Contact')
    attention_id = fields.Char(string="Attention/Contact")
    attention_id_arabic = fields.Char('Attention/Contact Arabic')
    pi_num = fields.Char("PI Number")
    ref_num = fields.Char(string='FGOC Ref', required=True, copy=False, readonly=True,
                       default=lambda self: _('New'))

    # @api.model
    # def create(self, vals):
    #     print(self.env.context)
    #     if self.env.context.get('default_move_type') != 'entry' and vals.get('ref_num', _('New')) == _('New'):
    #         vals['ref_num'] = self.env['ir.sequence'].next_by_code('account.sequence') or _('New')
    #         result = super(AccountMove, self).create(vals)
    #         return result

    # def action_ref_sequence_records(self, records):
    #     if records:
    #         invs = records.sorted(key=lambda r: r.id)
    #         for rec in invs:
    #             if rec.move_type != 'entry':
    #                 rec.write({'ref_num': self.env['ir.sequence'].next_by_code('account.sequence') or _('New')})

    @api.depends('amount_total')
    def _compute_total_amount_words(self):
        for invoice in self:
            invoice.total_amount_words = invoice.currency_id.amount_to_text(invoice.amount_total)

    total_amount_words = fields.Char("Total (In Words)", compute="_compute_total_amount_words")

    def invoice_amount_in_words(self, lang, amount):

        return self.currency_id.with_context(lang='ar_001').amount_to_text(amount)


    partner_vat = fields.Char(string='Partner Tax ID', related="partner_id.vat", store=True, index=True,
                              help="The Partner Tax Identification Number.")
    company_vat = fields.Char(string='Company Tax ID', related="partner_id.vat", store=True, index=True,
                              help="Your Company Tax Identification Number.")



    def action_invoice_sent(self):
        res = super(AccountMove, self).action_invoice_sent()
        template_id = self.env.ref('odx_electronic_invoice.email_template_electronic_invoice').id
        template = self.env['mail.template'].browse(template_id)
        res['context']['default_template_id'] = template_id
        return res


class AccountAccount(models.Model):
    _inherit = 'account.account'

    arabic_name = fields.Char(string='Arabic Name')


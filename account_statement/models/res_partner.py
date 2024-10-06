# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo.tools.float_utils import float_round as round
from odoo import api, fields, models, _
from datetime import datetime, time, date
from dateutil.relativedelta import relativedelta
from lxml import etree
import base64
import re
from odoo import tools
#import odoo.report
import calendar


class account_move(models.Model):
	
	_inherit = 'account.move'
	_order = 'invoice_date_due'
	
	def _get_result(self):
		for aml in self:
			aml.result = 0.0
			aml.result = aml.amount_total_signed - aml.credit_amount 

	def _get_credit(self):
		for aml in self:
			aml.credit_amount = 0.0
			aml.credit_amount = aml.amount_total_signed - aml.amount_residual_signed

	credit_amount = fields.Float(compute ='_get_credit',   string="Credit/paid")
	result = fields.Float(compute ='_get_result',   string="Balance") #'balance' field is not the same


class Res_Partner(models.Model):
	_inherit = 'res.partner'

	balance_invoice_ids = fields.One2many('account.move', 'partner_id', 'Customer move lines',
										  domain=[('move_type', 'in', ['out_invoice', 'out_refund']),
												  ('state', 'in', ['posted'])])

	payment_amount_due_amt = fields.Float(compute='_get_amounts_and_date_amount', string="Balance Due")
	payment_amount_overdue_amt = fields.Float(compute='_get_amounts_and_date_amount',
											  string="Total Overdue Amount")
	shop_name = fields.Char(string='Shop Name')

	def _get_amounts_and_date_amount(self):
		user_id = self._uid
		company = self.env['res.users'].browse(user_id).company_id

		current_date = datetime.now().date()

		for partner in self:
			# partner.do_process_monthly_statement_filter()
			amount_due = amount_overdue = 0.0
			supplier_amount_due = supplier_amount_overdue = 0.0
			for aml in partner.balance_invoice_ids:
				if (aml.company_id == company):
					date_maturity = aml.invoice_date_due or aml.date
					amount_due += aml.result
					if (date_maturity <= current_date):
						amount_overdue += aml.result
			partner.payment_amount_due_amt = amount_due
			partner.payment_amount_overdue_amt = amount_overdue

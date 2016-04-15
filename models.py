# -*- coding: utf-8 -*-

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp


class AccountDiscount(models.Model):
    _inherit = 'account.tax'

    is_discount = fields.Boolean('Is Discount', default=False)


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.one
    @api.depends('invoice_line.price_subtotal', 'tax_line.amount')
    def _compute_amount(self):
        self.amount_untaxed = sum(line.price_subtotal for line in self.invoice_line)
        self.amount_tax = sum(line.amount for line in self.tax_line if line.amount > 0)
        self.amount_discount = sum(line.amount for line in self.tax_line if line.amount < 0)
        self.amount_total = self.amount_untaxed + self.amount_tax + self.amount_discount

    amount_discount = fields.Float(string='Discount', digits=dp.get_precision('Account'), store=True, readonly=True,
                                   compute='_compute_amount')



# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
import calendar

class AccountPaymentTermLine(models.Model):
    _inherit = "account.payment.term.line"

    option = fields.Selection([
            ('day_after_invoice_date', 'Day(s) after the invoice date'),
            ('day_decade_after_invoice_date', u'Jour(s) décade après la date de facturation'),
            ('fix_day_following_month', 'Day(s) after the end of the invoice month (Net EOM)'),
            ('last_day_following_month', 'Last day of following month'),
            ('last_day_current_month', 'Last day of current month'),
        ],
        default='day_after_invoice_date', required=True, string='Options'
        )

class AccountPaymentTerm(models.Model):
    _inherit = "account.payment.term"

    @api.one
    def compute(self, value, date_ref=False):
        date_ref = date_ref or fields.Date.today()
        amount = value
        result = []
        if self.env.context.get('currency_id'):
            currency = self.env['res.currency'].browse(self.env.context['currency_id'])
        else:
            currency = self.env.user.company_id.currency_id
        prec = currency.decimal_places
        for line in self.line_ids:
            if line.value == 'fixed':
                amt = round(line.value_amount, prec)
            elif line.value == 'percent':
                amt = round(value * (line.value_amount / 100.0), prec)
            elif line.value == 'balance':
                amt = round(amount, prec)
            if amt:
                next_date = fields.Date.from_string(date_ref)
                if line.option == 'day_after_invoice_date':
                    next_date += relativedelta(days=line.days)
                elif line.option == 'day_decade_after_invoice_date':
                    next_date += relativedelta(days=line.days)
                    if next_date.day <= 10:
                        next_date = next_date.replace(day=10)
                    elif next_date.day <= 20:
                        next_date = next_date.replace(day=20)
                    else:
                        next_date = date(next_date.year, next_date.month, calendar.monthrange(next_date.year, next_date.month)[-1])
                        #next_date += relativedelta(days=14)
                        #next_date = next_date.replace(day=1)
                elif line.option == 'fix_day_following_month':
                    next_first_date = next_date + relativedelta(day=1, months=1)  # Getting 1st of next month
                    next_date = next_first_date + relativedelta(days=line.days - 1)
                elif line.option == 'last_day_following_month':
                    next_date += relativedelta(day=31, months=1)  # Getting last day of next month
                elif line.option == 'last_day_current_month':
                    next_date += relativedelta(day=31, months=0)  # Getting last day of next month
                result.append((fields.Date.to_string(next_date), amt))
                amount -= amt
        amount = reduce(lambda x, y: x + y[1], result, 0.0)
        dist = round(value - amount, prec)
        if dist:
            last_date = result and result[-1][0] or fields.Date.today()
            result.append((last_date, dist))
        return result


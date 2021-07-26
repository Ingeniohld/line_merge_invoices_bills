# -*- coding: utf-8 -*-
from odoo import api, models


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    def merge_invoice_line(self):
        move_id = self.env['account.move.line'].read_group([
            ('move_id', '=', self.id)],
            ['product_id', 'quantity'], ['product_id'])
        for record in move_id[:-1]:
            line_ids = self.env['account.move.line'].search([
                ('move_id', '=', self.id),
                ('product_id', '=', record['product_id'][0])])
            main_line = line_ids[0]
            line_ids[1:].with_context(check_move_validity=False).unlink()
            main_line.quantity = record['quantity']

    @api.model
    def create(self, vals):
        res = super(AccountMove, self).create(vals)
        if res.move_type == 'in_invoice' and self.env.user.company_id.auto_merge_bill_line:
            res.merge_invoice_line()
        if res.move_type == 'out_invoice' and self.env.user.company_id.auto_merge_invoice_line:
            res.merge_invoice_line()
        return res

    def write(self, vals):
        res = super(AccountMove, self).write(vals)
        if 'line_ids' in vals and self.move_type == 'in_invoice' and self.env.user.company_id.auto_merge_bill_line:
            self.merge_invoice_line()
        if 'line_ids' in vals and self.move_type == 'out_invoice' and self.env.user.company_id.auto_merge_invoice_line:
            self.merge_invoice_line()
        return res

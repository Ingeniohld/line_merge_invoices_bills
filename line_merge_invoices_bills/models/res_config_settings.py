# -*- coding: utf-8 -*-
from odoo import fields, models


class ResCompanyInherit(models.Model):
    _inherit = "res.company"

    auto_merge_invoice_line = fields.Boolean(string="Auto Merge Invoice Lines")
    auto_merge_bill_line = fields.Boolean(string="Auto Merge Bill Lines")


class ResConfigSettingsInherit(models.TransientModel):
    _inherit = 'res.config.settings'

    auto_merge_invoice_line = fields.Boolean(string="Auto Merge Invoice Lines", related='company_id.auto_merge_invoice_line', readonly=False)
    auto_merge_bill_line = fields.Boolean(string="Auto Merge Bill Lines", related='company_id.auto_merge_bill_line', readonly=False)

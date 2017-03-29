# -*- coding: utf-8 -*-
from odoo import fields, models


class CrmIndustry(models.Model):
    _name = 'crm.industry'
    _description = 'CRM Industry'
    _order = "name asc"

    name = fields.Char(string='Industry Name',required=True)
    state = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], string='Status', default='active')

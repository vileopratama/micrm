# -*- coding: utf-8 -*-
from odoo import fields, models


class CrmService(models.Model):
    _name = 'crm.service'
    _description = 'CRM Service'
    _order = "name asc"

    name = fields.Char(string='Service Name',required=True)
    state = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], string='Status', default='active')

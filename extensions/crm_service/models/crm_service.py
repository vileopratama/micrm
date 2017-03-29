# -*- coding: utf-8 -*-
from odoo import fields, models, api


class CrmService(models.Model):
    _name = 'crm.service'
    _description = 'CRM Service'
    _order = "name asc"

    name = fields.Char(string='Service Name',required=True)
    state = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], string='Status', default='active')

    @api.multi
    def action_active(self):
        return self.write({'state': 'active'})

    @api.multi
    def action_inactive(self):
        return self.write({'state': 'inactive'})

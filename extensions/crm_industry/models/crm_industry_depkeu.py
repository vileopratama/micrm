# -*- coding: utf-8 -*-
from odoo import fields, models, api


class IndustryDepkeu(models.Model):
    _name = 'crm.industry.depkeu'
    _description = 'CRM Depkeu Industry'
    _order = "name asc"

    name = fields.Char(string='Industry Name',required=True)
    state = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], string='Status', default='active')

    _sql_constraints = [
        ('unique_name', 'unique (name)', 'Industry must be unique!'),
    ]

    @api.multi
    def action_active(self):
        return self.write({'state': 'active'})

    @api.multi
    def action_inactive(self):
        return self.write({'state': 'inactive'})

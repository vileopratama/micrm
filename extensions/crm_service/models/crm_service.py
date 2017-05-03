# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Service(models.Model):
    _name = 'crm.service'
    _description = 'CRM Service'
    _order = "name asc"

    name = fields.Char(string='Service Name', required=True)
    state = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], string='Status', default='active')
    type = fields.Selection([('audit-assurance', 'Audit & Assurance'), ('bso', 'Business Services & Outsourcing (BSO)'),
                             ('ras', 'Risk Advisory Services (RAS)'), ('it-advisory', 'IT Advisory'), ('tax', 'Tax'),
                             ('kjpp', 'KJPP')], string='Group', default='audit-assurance')

    _sql_constraints = [
        ('unique_name', 'unique (name)', 'Service must be unique!'),
    ]

    @api.multi
    def action_active(self):
        return self.write({'state': 'active'})

    @api.multi
    def action_inactive(self):
        return self.write({'state': 'inactive'})

# -*- coding: utf-8 -*-

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Customer'
    _order = "name asc"

    audit_assurance_service_ids = fields.Many2many('crm.service', 'res_partner_service_rel',
                                                   'partner_id', 'service_id', string='Audit &amp; Assurance',
                                                   domain="[('type', '=', 'audit-assurance' )]", )

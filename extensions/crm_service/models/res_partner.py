# -*- coding: utf-8 -*-

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Customer'
    _order = "name asc"

    audit_assurance_service_ids = fields.Many2many('crm.service', 'res_partner_service_audit_assurance',
                                                   'partner_id', 'service_id', string='Audit &amp; Assurance',
                                                   domain="[('type', '=', 'audit_assurance' )]")
    bso_service_ids = fields.Many2many('crm.service', 'res_partner_service_bso',
                                                   'partner_id', 'service_id', string='Business Services & Outsourcing',
                                                   domain="[('type', '=', 'bso' )]" )
    ras_service_ids = fields.Many2many('crm.service', 'res_partner_service_ras',
                                       'partner_id', 'service_id', string='Risk Advisory Services',
                                       domain="[('type', '=', 'ras' )]" )
    it_advisory_service_ids = fields.Many2many('crm.service', 'res_partner_service_it_advisory',
                                       'partner_id', 'service_id', string='IT Advisory',
                                       domain="[('type', '=', 'it-advisory' )]" )
    tax_service_ids = fields.Many2many('crm.service', 'res_partner_service_tax',
                                       'partner_id', 'service_id', string='Tax',
                                       domain="[('type', '=', 'tax' )]" )
    kjpp_service_ids = fields.Many2many('crm.service', 'res_partner_service_kjpp',
                               'partner_id', 'service_id', string='KJPP',
                               domain="[('type', '=', 'kjpp' )]" )


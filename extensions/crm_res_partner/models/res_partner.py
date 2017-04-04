# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Customer'

    contact_person = fields.Char(string='Contact Person')
    listed = fields.Selection([('listed', 'Listed'), ('non-listed', 'Non Listed')], string='Listed/Non Listed',
                              default='listed')
    referral = fields.Selection([('referral', 'Referral'), ('non-referral', 'Non Referral')], string='Referral/Non Referral',
                              default='referral')
    local = fields.Selection([('local', 'Local'), ('international', 'International')],
                                string='Local/International',
                                default='local')
    revenue = fields.Float(string='Revenue')


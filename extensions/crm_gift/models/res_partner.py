# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Customer'

    gift_count = fields.Integer(string="Gift", compute='_compute_gift_count')

    @api.multi
    def _compute_gift_count(self):
        for partner in self:
            operator = 'child_of' if partner.is_company else '='
            partner.gift_count = self.env['crm.gift'].search_count(
            [('partner_id', operator, partner.id)])

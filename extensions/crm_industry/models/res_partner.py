# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Customer'
    _order = "name asc"

    industry_id = fields.Many2one(comodel_name='crm.industry',string='Industry')
    industry_depkeu_id = fields.Many2one(comodel_name='crm.industry.depkeu', string='Depkeu Industry')

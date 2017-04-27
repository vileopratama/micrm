# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Customer'

    date_founding = fields.Date(string='Founding Date', required=True, copy=False)
    contact_person = fields.Char(string='Contact Person')
    listed = fields.Selection([('listed', 'Listed'), ('non-listed', 'Non Listed')], string='Listed/Non Listed',
                              default='listed')
    referral = fields.Selection([('referral', 'Referral'), ('non-referral', 'Non Referral')], string='Referral/Non Referral',
                              default='referral')
    local = fields.Selection([('local', 'Local'), ('international', 'International')],
                                string='Local/International',
                                default='local')
    revenue = fields.Float(string='Revenue')
    peoples = fields.One2many(comodel_name='res.partner.peoples', inverse_name='partner_id', string='Management',
                              copy=True)

class ResPartnerPeople(models.Model):
    _name = "res.partner.peoples"
    _description = "Management"
    _rec_name = "name"

    partner_id = fields.Many2one('res.partner', string='Client', ondelete='cascade')
    name = fields.Char(string='Name', required=True, copy=False)
    job_id = fields.Many2one(comodel_name='hr.job',string='Title', required=True, copy=False)
    date_birth = fields.Date(string='Birthdate', required=True, copy=False)
    state = fields.Selection(selection=[('active','Active'),('inactive','Inactive')],string='State',default='active')


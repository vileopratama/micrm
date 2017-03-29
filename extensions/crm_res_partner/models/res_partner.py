# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Customer'

    contact_person = fields.Char(string='Contact Person')
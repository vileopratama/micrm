# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class res_company(models.Model):
    _inherit = 'res.company'
    birthday_mail_template = fields.Many2one('mail.template', string='Birthday Wishes Template',
                                             help="This will set the default mail template for birthday wishes.")

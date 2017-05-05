# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    birthday_mail_template = fields.Many2one('mail.template', string='Birthday Wishes Template',
                                             help="This will set the default mail template for birthday wishes.")
    birthday_people_mail_template = fields.Many2one('mail.template', string='Birthday Management Wishes Template',
                                             help="This will set the default mail template for birthday wishes Client Management.")

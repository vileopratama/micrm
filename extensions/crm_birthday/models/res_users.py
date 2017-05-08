# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime, timedelta, time


class ResUser(models.Model):
    _inherit = 'res.users'

    notif_mail_client_birthday = fields.Boolean(string='Notif Mail Client Birthday',default=False)

    @api.multi
    def send_mail_notif(self):
        ir_data = self.env['ir.model.data']
        base_template = ir_data.get_object('crm_birthday', 'email_user_notif_client_birthday_template')
        channel = ir_data.get_object('crm_birthday', 'channel_user_notif_client_birthday')
        today = datetime.now()
        today_month_day = '%-' + today.strftime('%m') + '-' + today.strftime('%d')

        for partner in self.env['res.partner'].search([('date_founding', 'like', today_month_day)]):
            for user in self.env['res.users'].search([('notif_mail_client_birthday', '=', True)]):
                if user.email:
                    if user.company_id.notif_birthday_mail_template and user.company_id.notif_birthday_mail_template.id:
                        user.company_id.notif_birthday_mail_template.sudo().send_mail(user.id, force_send=True)
                    else:
                        base_template.sudo().send_mail(user.id, force_send=True)

                res = channel.message_post(body=_('Happy Birthday Dear %s.') % (user.name), user_ids=[user.id])
                res.write({'channel_ids': [[6, False, [channel.id]]]})
                user.message_post(body=_('Notif User.'))

        return None

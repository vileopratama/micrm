# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime, timedelta, time


class ResUser(models.Model):
    _inherit = 'res.users'

    notif_mail_client_birthday = fields.Boolean(string='Notif Mail Client Birthday', default=False)

    @api.multi
    def send_mail_notif(self):
        email_obj = self.env.get('mail.template')
        emails = email_obj.search([('name', '=', 'User Notif Client Birthday')])

        today = datetime.now()
        today_month_day = '%-' + today.strftime('%m') + '-' + today.strftime('%d')

        sql = " select name,to_char((date_founding), 'DD/MM/YYYY') as date_founding " \
              " FROM res_partner  " \
              " WHERE to_char((date_founding - interval '7 day'), 'YYYY-MM-DD') LIKE '%" + today_month_day + "%' "
        self.env.cr.execute(sql)
        partners = self.env.cr.dictfetchall()

        for partner in partners:
            for email in emails:
                for user in self.env['res.users'].search([('notif_mail_client_birthday', '=', True)]):
                    email.write({
                        'email_from': 'no-reply@bdo.co.id',
                        'email_to': user.email,
                        'subject': 'CRM BDOMI - Client Birthday',
                        'body_html': _('Dear %s.') % (user.name) + '<br/><br/>' + _('Client %s.') % (partner['name']) +
                                     _('Is Birthday in %s.') % (partner['date_founding']),
                    })
                    email.sudo().send_mail(1, force_send=True)

        sql = " select res_partner_peoples.name,res_partner.name as client_name,to_char((res_partner_peoples.date_birth), 'DD/MM/YYYY') as date_birth " \
              " FROM res_partner_peoples " \
              " inner join res_partner on (res_partner.id = res_partner_peoples.partner_id) " \
              " WHERE to_char((date_birth - interval '7 day'), 'YYYY-MM-DD') LIKE '%" + today_month_day + "%'; "
        self.env.cr.execute(sql)
        partner_peoples = self.env.cr.dictfetchall()

        for partner_people in partner_peoples:
            for email in emails:
                for user in self.env['res.users'].search([('notif_mail_client_birthday', '=', True)]):
                    email.write({
                        'email_from': 'no-reply@bdo.co.id',
                        'email_to': user.email,
                        'subject': 'CRM BDOMI - Client Birthday',
                        'body_html': _('Dear %s.') % (user.name) + '<br/><br/>' + _('People %s.') % (
                            partner_people['name'])
                                     + _(' of the Client %s.') % (partner_people['client_name']) + _(
                            'Is Birthday in %s.') % (partner_people['date_birth']),
                    })
                    email.sudo().send_mail(1, force_send=True)

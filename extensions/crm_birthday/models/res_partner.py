# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime, timedelta, time


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.multi
    def send_partner_birthday_email(self):
        ir_data = self.env['ir.model.data']
        base_template = ir_data.get_object('crm_birthday', 'email_partner_template_birthday')
        channel = ir_data.get_object('crm_birthday', 'channel_partner_birthday')
        today = datetime.now()
        today_month_day = '%-' + today.strftime('%m') + '-' + today.strftime('%d')

        for partner in self.search([('date_founding', 'like', today_month_day)]):
            if partner.email:
                if partner.company_id.birthday_mail_template and partner.company_id.birthday_mail_template.id:
                    partner.company_id.birthday_mail_template.sudo().send_mail(partner.id, force_send=True)
                else:
                    base_template.sudo().send_mail(partner.id, force_send=True)

            res = channel.message_post(body=_('Happy Birthday Dear %s.') % (partner.name), partner_ids=[partner.id])
            res.write({'channel_ids': [[6, False, [channel.id]]]})
            partner.message_post(body=_('Happy Birthday.'))

        return None


class ResPartnerPeople(models.Model):
    _inherit = 'res.partner.peoples'

    def send_partner_people_birthday_email(self):
        ir_data = self.env['ir.model.data']
        base_template = ir_data.get_object('crm_birthday', 'email_partner_people_template_birthday')
        channel = ir_data.get_object('crm_birthday', 'channel_partner_people_birthday')
        today = datetime.now()
        today_month_day = '%-' + today.strftime('%m') + '-' + today.strftime('%d')

        for people in self.search([('date_birth', 'like', today_month_day)]):
            if people.email:
                if people.partner_id.company_id.birthday_people_mail_template and people.partner_id.company_id.birthday_people_mail_template.id:
                    people.partner_id.company_id.birthday_people_mail_template.sudo().send_mail(people.id, force_send=True)
                else:
                    base_template.sudo().send_mail(people.id, force_send=True)

            res = channel.message_post(body=_('Happy Birthday Dear %s.') % (people.name), partner_ids=[people.id])
            res.write({'channel_ids': [[6, False, [channel.id]]]})
            people.message_post(body=_('Happy Birthday.'))

        return None
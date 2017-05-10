# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime as dt,date,timedelta, time


class ResPartner(models.Model):
    _inherit = 'res.partner'

    date_notif = fields.Date(compute='_compute_date_notif', string='Date of notif', readonly=True,)

    @api.multi
    @api.depends('date_founding')
    def _compute_date_notif(self):
        for partner in self:
            if partner.date_founding:
                date_founding = partner.date_founding
                date_founding = dt.strptime(date_founding, "%Y-%m-%d")
                date_notif = date_founding - timedelta(days=7)
                partner.date_notif = date_notif.strftime('%Y-%m-%d')


    @api.multi
    def send_partner_birthday_email(self):
        ir_data = self.env['ir.model.data']
        base_template = ir_data.get_object('crm_birthday', 'email_partner_template_birthday')
        channel = ir_data.get_object('crm_birthday', 'channel_partner_birthday')
        today = dt.now()
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

    date_notif = fields.Date(compute='_compute_date_notif', string='Date of notif', readonly=True,)

    @api.multi
    @api.depends('date_birth')
    def _compute_date_notif(self):
        for partner in self:
            if partner.date_birth:
                date_birth = partner.date_birth
                date_birth = dt.strptime(date_birth, "%Y-%m-%d")
                date_notif = date_birth - timedelta(days=7)
                partner.date_notif = date_notif.strftime('%Y-%m-%d')



    def send_partner_people_birthday_email(self):
        ir_data = self.env['ir.model.data']
        base_template = ir_data.get_object('crm_birthday', 'email_partner_people_template_birthday')
        channel = ir_data.get_object('crm_birthday', 'channel_partner_people_birthday')
        today = dt.now()
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
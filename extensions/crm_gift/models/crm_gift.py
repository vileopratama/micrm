# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Gift(models.Model):
    _name = 'crm.gift'
    _description = 'Gift for Client Birthdate'
    _rec_name = 'name'

    partner_id = fields.Many2one(comodel_name='res.partner', string='Client', ondelete='restrict', store=True,
                                 required=True)
    partner_people_id = fields.Many2one(comodel_name='res.partner.peoples', string='People', ondelete='restrict',
                                        store=True, required=True)
    name = fields.Char(string='Gift name', required=True)
    image = fields.Binary("Image", attachment=True,
                          help="This field holds the image used as avatar for this contact, limited to 1024x1024px")
    image_medium = fields.Binary("Medium-sized image", attachment=True,
                                 help="Medium-sized image of this contact. It is automatically " \
                                      "resized as a 128x128px image, with aspect ratio preserved. " \
                                      "Use this field in form views or some kanban views.")
    state = fields.Selection(selection=[('plan', 'Plan'), ('sent', 'Sent')], default='sent', string='State')
    note = fields.Text(string='Note')
    date_submission = fields.Date(string='Date of submission', required=True, copy=False)

    @api.onchange('partner_id')
    def _onchange_partner_people_id(self):
        if self.partner_id:
            return {'domain': {'partner_people_id': [('partner_id', '=', self.partner_id.id)]}}
        else:
            return {'domain': {'partner_people_id': [('partner_id', '=', 0)]}}
			


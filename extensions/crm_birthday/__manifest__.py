# -*- coding: utf-8 -*-
{
    "name": "CRM Birthday Wish Notif to Client",
    "version": "10.0.0.1",
    "author": "Suhendar",
    "category": "Other",
    "website": "http://bdo.co.id",
    "description": """In any business customer relations are most important and for any one their bithday is alwasy special so wish your clients using this module and improve your relations. Send Birthday Wishes via mail, get birthday Notifications and wish your customers.""",
    "summary": "Send Birthday Wishes via mail, get birthday Notifications and wish your customers",
    "license": "AGPL-3",
    "depends": ['crm_res_partner','mail'],
    'data': [
        'migrate/template_migrate.xml',
        'views/res_config_view.xml',
        'scheduler/res_partner_scheduler.xml',
        'views/res_users_view.xml',
    ],
    'images': [

    ],
    "installable": True,
    "auto_install": False,
}

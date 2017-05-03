# -*- coding: utf-8 -*-
{
    'name' : 'BDO CRM Updated For Client Management Gift',
    'version' : '10.0.1.1.0',
    'author' : 'Suhendar',
    'category' : 'CRM',
    'summary': 'CRM Client Gift',
    'website' : 'http://www.bdo.co.id',
    'description': """
        Add gift menu for Client 
    """,
    'depends' : ['crm'],
    'data' : [
        'views/crm_gift_view.xml',
		'views/res_partner_view.xml',
    ],
    'installable': True,
    'application' : False,
    'auto_install' : False
}

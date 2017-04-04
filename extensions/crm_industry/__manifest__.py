# -*- coding: utf-8 -*-
{
    'name' : 'CRM Industry For MI CRM',
    'version' : '10.0.1.1.0',
    'author' : 'Suhendar',
    'category' : 'CRM',
    'summary': 'CRM Industry',
    'website' : 'http://www.bdo.co.id',
    'description': """
        Classification Clients/Customer by Industry
    """,
    'depends' : ['crm'],
    'data' :[
        'security/ir.model.access.csv',
        'views/crm_industry_view.xml',
        'views/crm_industry_depkeu_view.xml',
        'views/res_partner_view.xml',
    ],
    'installable': True,
    'application' : False,
    'auto_install' : False
}

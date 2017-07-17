# -*- coding: utf-8 -*-
{
    'name' : 'BDO CRM Updated For Res Partner',
    'version' : '10.0.1.1.0',
    'author' : 'Suhendar',
    'category' : 'CRM',
    'summary': 'CRM Res Partner',
    'website' : 'http://www.bdo.co.id',
    'description': """
        Updated field customers 
    """,
    'depends' : ['hr'],
    'data' : [
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
    ],
    'installable': True,
    'application' : False,
    'auto_install' : False
}

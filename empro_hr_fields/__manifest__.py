# -*- coding: utf-8 -*-
{
    'name': "HR Fields Empro Ltda - V2",

    'summary': """
        Campos agregados para poder ser utilizados en la parte de RRHH de EMPRO LTDA kanban""",

    'description': """
        Campos agregados para poder ser utilizados en la parte de RRHH de EMPRO LTDA. Odoo V11 kanban $ views
    """,

    'author': "Empro Ltda",
    'website': "http://www.emproltda.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.18011709',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,

}
# -*- coding: utf-8 -*-
{
    'name': "HR Attendance uses project location Empro Ltda ",

    'summary': """
        Campos agregados para poder ser utilizados en la parte de asistencia de RRHH de EMPRO LTDA""",

    'description': """
        Campos agregados para poder ser utilizados en la parte de RRHH de EMPRO LTDA. asistencia
        view updated, added widget url 2018006201713
    """,

    'author': "Empro Ltda",
    'website': "http://www.emproltda.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.18006201713',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': False,

}
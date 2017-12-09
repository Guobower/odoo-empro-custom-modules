# -*- coding: utf-8 -*-
from odoo import models, fields, api, tools
import time
import datetime
from odoo.tools.translate import _
from dateutil.relativedelta import relativedelta

def str_to_datetime(strdate):
    return datetime.datetime.strptime(strdate, tools.DEFAULT_SERVER_DATE_FORMAT)

class empro_employee(models.Model):
    _inherit = "hr.employee"

    _columns = {
        'employee_code': fields.Char('Codigo Empro', required=True),
        'legal_name': fields.Char('Nombre Legal'),
        'personal_email': fields.Char('Email Personal'),
        'personal_phone': fields.Char('Telefono Personal'),
        'personal_mobile': fields.Char('Celular Personal'),
        'personal_address': fields.Char('Direccion Personal'),
        'dependents_count': fields.Integer('Numero de Dependientes'),
        'spouse_name': fields.Char('Nombre del Conyuge'),
        'emergency_contact': fields.Char('Contacto de Emergencia'),
        'driver_license': fields.Char('Licencia de Conducir'),
        'driver_license_expiration' : fields.Date("Expiracion Licencia de Conducir"),
        'interview_date' : fields.Date("Fecha de entrevista"),
        'start_date' : fields.Date("Fecha de Inicio", required=True),
        'end_date' : fields.Date("Fecha de Salida"),
        'exit_reason': fields.Char('Razon de Salida'),
        'years_hired': fields.Integer('Anos Contratados'),
        'months_hired': fields.Integer('Meses Contratados'),
        'days_hired': fields.Integer('Dias Contratados'),
        'start_project': fields.Char('Primer Proyecto'),
        'last_settlement' : fields.Date("Ultima Liquidacion"),
        'years_settlement': fields.Integer('Anos para liquidacion'),
        'months_settlement': fields.Integer('Meses para liquidacion'),
        'days_settlement': fields.Integer('Dias para liquidacion')
    }

    _defaults ={
        'start_date': datetime.date.today()
    }

    @api.onchange('start_date')
    def set_antiguedad(self):
        if self.start_date:
            start_date = str_to_datetime(self.start_date)
            today_date = datetime.datetime.now()
            rd = relativedelta(today_date, start_date)
            self.years_hired = rd.years
            self.months_hired = rd.months
            self.days_hired = rd.days

    @api.onchange('last_settlement')
    def set_liquidacion(self):
        if self.start_date:
            last_settlement = str_to_datetime(self.last_settlement)
            today_date = datetime.datetime.date()
            rd = relativedelta(today_date, last_settlement)
            self.years_settlement = rd.years
            self.months_settlement = rd.months
            self.days_settlement = rd.days

empro_employee()
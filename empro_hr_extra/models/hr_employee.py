# -*- coding: utf-8 -*-

from odoo import models, fields

class HrEmployee(models.Model):
	_name = 'hr.employee'
	_inherit = 'hr.employee'

	employee_code : fields.Char('Codigo Empro', required=True)
	legal_name : fields.Char('Nombre Legal')
	personal_email : fields.Char('Email Personal')
	personal_phone : fields.Char('Telefono Personal')
	personal_mobile : fields.Char('Celular Personal')
	personal_address: fields.Char('Direccion Personal')
	dependents_count: fields.Integer('Numero de Dependientes')
	spouse_name: fields.Char('Nombre del Conyuge')
	emergency_contact: fields.Char('Contacto de Emergencia')
	driver_license: fields.Char('Licencia de Conducir')
	driver_license_expiration : fields.Date("Expiracion Licencia de Conducir")
	interview_date : fields.Date("Fecha de entrevista")
	start_date : fields.Date("Fecha de Inicio", required=True)
	end_date : fields.Date("Fecha de Salida")
	exit_reason: fields.Char('Razon de Salida')
	years_hired: fields.Integer('Anos Contratados')
	months_hired: fields.Integer('Meses Contratados')
	days_hired: fields.Integer('Dias Contratados')
	start_project: fields.Char('Primer Proyecto')
	last_settlement : fields.Date("Ultima Liquidacion")
	years_settlement: fields.Integer('Anos para liquidacion')
	months_settlement: fields.Integer('Meses para liquidacion')
	day_settlement: fields.Integer('Dias para liquidacion')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

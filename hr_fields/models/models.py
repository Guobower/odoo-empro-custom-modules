# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrEmployee(models.Model):
	_inherit = 'hr.employee'
	#_name = 'hr_fields.hr_fields'

	x_emp_employee_code = fields.Char('Codigo Empro')
	x_emp_legal_name =  fields.Char('Nombre Legal')
	x_emp_personal_email = fields.Char('Email Personal')
	x_emp_personal_phone = fields.Char('Telefono Personal')
	x_emp_personal_mobile = fields.Char('Celular Personal')
	x_emp_cns_afiliado = fields.Boolean('Afiliado en la CNS')
	x_emp_google_drive_url = fields.Char('Url File en GDrive')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

# class test_module(models.Model):
#     _name = 'test_module.test_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hr_fields(models.Model):
	_inherit = 'hr.employee'
	#_name = 'hr_fields.hr_fields'

	employee_code = fields.Char('Codigo Empro', required=True)
	legal_name =  fields.Char('Nombre Legal')
	personal_email = fields.Char('Email Personal')
	personal_phone = fields.Char('Telefono Personal')
	personal_mobile = fields.Char('Celular Personal')
	CNS_afiliado = fields.Boolean('Afiliado en la CNS')

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
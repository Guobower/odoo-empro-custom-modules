# -*- coding: utf-8 -*-

from odoo import models, fields

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'
    
    # datos generales
    x_proyecto_asignado_id = fields.Many2one('project.project', string='Proyecto Asignado')
    x_fase_asignado_id = fields.Many2one('project.task', string='Fase Asignado')
    x_comentarios_del_dia_de_asistencia = fields.Char('Comentarios del dia')
    x_biometrico = fields.Selection(string='Biometrico',selection=[( '105','EMPRO Lagunillas'), ( 'CAM', 'EMPRO Camiri'), ('SCZ','Emro Santa Cruz'), ('CBB','Empro Oficina Central'), ('110','Empro Tamborada'), ('109','Empro Nancahuazu'),('114','Empro Catering'), ( 'ICS5','EMPRO ICS5')])
    x_es_descanso = fields.Boolean('Es descanso?')
    x_es_falta_justificada = fields.Boolean('Es falta justificada?')
    x_es_falta_no_justificada = fields.Boolean('Es falta no justificada?')
    x_es_haber_basico = fields.Boolean('Es con pago de haber basico?')
    x_es_vacacion = fields.Boolean('Es vacacion?')

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
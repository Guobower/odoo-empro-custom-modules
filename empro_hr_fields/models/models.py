# -*- coding: utf-8 -*-

from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    #_name = 'empro_hr_fields.hr_'
    
    # datos generales
    x_employee_code = fields.Char('Codigo Empro', default="EMP_")
    x_legal_name =  fields.Char('Nombre Legal')
    x_personal_email = fields.Char('Email Personal')
    x_personal_phone = fields.Char('Telefono Personal')
    x_personal_mobile = fields.Char('Celular Personal')
    x_google_drive_url = fields.Char('Url File en GDrive')
    x_personal_nombre_emergencia = fields.Char('Nombre en caso de Emergencia')
    x_personal_telefono_emergencia = fields.Char('Telefono en caso de Emergencia')
    x_alergias = fields.Char('Alergias')
    x_factor_sanguineo = fields.Char('Factor Sanguineo')
    x_cns_afiliado = fields.Boolean('Afiliado en la CNS')
    x_seguro_de_vida = fields.Boolean('Tiene Seguro de Vida')
    x_seguro_de_accidente = fields.Boolean('Tiene Seguro de Accidentes')
    x_proyecto_asignado_id = fields.Many2one('project.project', string='Proyecto Asignado')
    x_fase_asignado_id = fields.Many2one('project.task', string='Fase Asignado')
    x_es_externo = fields.Boolean('Es Personal Externo')
    x_residencia = fields.Char('Residencia')

    # datos para control y renovacion 
    x_tetanos_fecha_primera_vacuna = fields.Date('Primera Vacuna Tetanos')
    x_tetanos_fecha_segunda_vacuna = fields.Date('Segunda Vacuna Tetanos')
    x_tetanos_fecha_tercera_vacuna = fields.Date('Tercera Vacuna Tetanos')
    x_tetanos_fecha_cuarta_vacuna = fields.Date('Cuarta Vacuna Tetanos')
    x_tetanos_fecha_quinta_vacuna = fields.Date('Quinta Vacuna Tetanos')
    x_tetanos_fecha_renovacion_vacuna = fields.Date('Fecha de Renovacion de Vacuna de Tetanos')
    x_fiebre_amarilla_fecha_renovacion_vacuna = fields.Date('Fecha de Renovacion de Vacuna de Fiebre Amarilla')
    x_fiebre_amarilla_fecha_vacuna = fields.Date('Fecha de Vacuna de Fiebre Amarilla')
    x_expiracion_ci = fields.Date('Fecha de expiracion de CI')
    x_expiracion_licencia_de_conducir = fields.Date('Fecha de expiracion de licencia de conducir')
    x_categoria_licencia_de_conducir = fields.Char('Categoria de licencia de conducir')
    x_expiracion_manejo_defensivo = fields.Date('Fecha de expiracion de manejo defensivo')
    x_expiracion_de_examen_ocupacional = fields.Date('Fecha de expiracion de examen ocupacional')
    x_expiracion_de_examen_complementarios = fields.Date('Fecha de expiracion de examenes complementarios')
    x_expiracion_seguro_de_vida = fields.Date('Fecha de expiracion de seguro de vida')
    x_expiracion_seguro_de_accidentes = fields.Date('Fecha de expiracion de seguro de accidentes')
    x_expiracion_credencial = fields.Date('Fecha de expiracion de credencial')
    x_hepatitis_fecha_primera_vacuna = fields.Date('Primera Vacuna Hepatitis')
    x_hepatitis_fecha_segunda_vacuna = fields.Date('Segunda Vacuna Hepatitis')
    x_hepatitis_fecha_terera_vacuna = fields.Date('Tercera Vacuna Hepatitis')
    x_carnet_sanitario = fields.Date('Fecha de Carnet sanitario')
    x_expiracion_carnet_sanitario = fields.Date('Fecha de Expiracion de Carnet sanitario')
    x_expiracion_hepatitis_fecha_primera_vacuna = fields.Date('Fecha de Expiracion Primera Vacuna Hepatitis')
    x_expiracion_hepatitis_fecha_segunda_vacuna = fields.Date('Fecha de Expiracion Segunda Vacuna Hepatitis')
    x_expiracion_hepatitis_fecha_terera_vacuna = fields.Date('Fecha de Expiracion Tercera Vacuna Hepatitis')

    # ficha de registro EMPRO
    x_carnet_Identidad = fields.Char('Carnet de Identidad')
    x_ci_emitido_en = fields.Char('CI Emitido en')
    x_licencia_de_conducir = fields.Char('Numero de licencia de conducir')
    x_haber_basico = fields.Float('Haber Basico')
    x_liquido_pagable = fields.Float('Liquido Pagable')
    x_total_ganado_esperado = fields.Char('Total Ganado Esperado (real)')
    x_fecha_de_ingreso = fields.Date('Fecha de Ingreso')
    x_fecha_de_contrato = fields.Date('Fecha de Contrato')
    x_cargo = fields.Char('Cargo')
    x_institucion_emisora_de_manejo_defensivo = fields.Char('Institucion emisora de manejo defensivo')

    # campos utiles para retiro de personal
    x_requiere_liquidacion_interna = fields.Boolean('Requiere liquidacion interna')
    x_modalidad_de_trabajo = fields.Selection(string='Modalidad de Trabajo', selection=[( 'Oficina','Trabajo en horarios de Oficina'),( '25/7', '25 Trabajo/7 Descanso'),  ( '21/7', '21 Trabajo/7 Descanso'), ('14/14','14 Trabajo/14 Descanso'), ('Lun-Vie','Lunes a Viernes')])

    # campos adicionales importantes

    # campos de la comunidad a tener para reporte mol
    x_mol = fields.Boolean('Es personal de la comunidad')
    x_mol_numero_requerimiento = fields.Char('Requerimiento MOL')
    x_mol_fecha_de_envio_de_requerimiento = fields.Date('Fecha de Envio de Requerimiento')
    x_mol_fecha_de_recepcion_de_listado_mol = fields.Date('Fecha de Recepcion de Listado MOL')
    x_mol_aval = fields.Char('Aval Institucion/Organizacion MOL')
    x_mol_contacto_de_aval = fields.Char('Personal de Contacto Aval MOL')
    x_mol_comunidad = fields.Char('Comunidad MOL')
    x_mol_residencia = fields.Char('Residencia MOL')
    x_mol_tipo_cargo = fields.Selection(string='MOL Tipo Cargo',selection=[('no-calificada', 'No Calificada'), ('semi-calificada', 'Semi Calificada'), ('calificada', 'Calificada'), ('directo', 'Directo')])
    x_mol_fecha_de_contrato = fields.Date('Fecha de Contrato MOL')
    x_mol_fecha_de_retiro = fields.Date('Fecha de Retiro MOL')
    x_mol_fue_retirado = fields.Boolean('Es personal retirado de la comunidad')
    x_mol_se_presento_documentacion = fields.Boolean('Se presento la documentacion a fiscalizacion')
    x_mol_observaciones = fields.Char('Observaciones MOL')

    

#    x_empro_contratos = fields.One2many(
#        'hr.employee.empro.contracts.line',
#        'employee_id',
#        string='Lineas de contratos',
#        copy=True,
#    )

#class HrEmployeeEmproContracts.line(models.Model):
#    _name='hr.employee.empro.contracts.line'
#    _description='Contratos pasados con EMPRO'
#
#    x_empro_contrato_finalizado = fields.Boolean('Finalizado')
#    x_empro_contrato_comentario = fields.Char('Comentario')
#    x_empro_contrato_inicio = fields.Date('Fecha inicio')
#    x_empro_contrato_fin = fields.Date('Fecha Fin')  
#    x_empro_contrato_proyecto = fields.Char('Proyecto')


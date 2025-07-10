from odoo import models, fields, api

class Ticket(models.Model):
    _name = 'soporte.ticket'
    _description = 'Ticket de soporte técnico'
    _order = 'fecha_creacion desc'

    nombre = fields.Char(string='Título del Problema', required=True)
    descripcion = fields.Char(string='Descripción detallada')

    estado = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('en_proceso', 'En Proceso'),
        ('resuelto', 'Resuelto'),
        ('cerrado', 'Cerrado'),
    ], string = 'Estado', default='nuevo')

    tecnico_id = fields.Many2one('res.users', string = 'Técnico asignado')

    fecha_creacion = fields.Datetime(string = 'Fecha de creación', default=fields.Datetime.now)
    fecha_resolucion = fields.Datetime(string = 'Fecha de resolución')

    @api.onchange('estado')
    def _onchange_estado(self):
        if self.estado == 'resuelto' and not self.fecha_resolucion:
            self.fecha_resolucion = fields.Datetime.now()
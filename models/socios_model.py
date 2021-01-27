from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date, datetime

class socios_model(models.Model):
    _name = 'cooperativa.socios_model'
    _description = 'modelo de socio'
    #limitamos id socio y dni
    _sql_constraints = [('socios_id_socio_uniq','UNIQUE (id_socio)','No puede haber dos socios con el mismo id'),('socios_dni_uniq','UNIQUE (dni)','No puede haber dos socios con el mismo dni'),]

    id_socio=fields.Integer(string="ID_socio", required=True)
    foto = fields.Binary(string="Foto", required=False)
    name = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    dni = fields.Char(string="DNI", required=True)
    fechaAlta = fields.Date(string="Fecha de alta", required=True, default=date.today())
    telf = fields.Char(string="Teléfono", required=True)
    email = fields.Char(string="Email", required=False)
    saldo = fields.Float(string="Saldo", required=False, readonly=True)
    registros = fields.One2many("cooperativa.campanya_model","id_socio", string="Registros Pendientes")

    @api.constrains("dni")
    def _comprobarDNI(self):
        if len(self.dni)!=9:
            raise ValidationError("El DNI debe tener 9 carácteres!")
        else:
            try:
                n=int(self.dni[:-1])
            except ValueError:
                raise ValidationError("Los primeros 8 dígitos deben ser números")

            palabra='TRWAGMYFPDXBNJZSQVHLCKE'

            if self.dni[-1].upper() == palabra[n%23]:
                return True
            else:
                
                raise ValidationError("Letra errónea")

    @api.constrains("email")
    def _comprobarEmail(self):
        if "@" not in self.email and len(self.email)<6:
            raise ValidationError("Email incorrecto. Debe contener una @, y más de 5 carácteres!")

    @api.constrains("telf")
    def _validaTelf(self):
        if len(self.telf)!=9:
            raise ValidationError("Longitud del teléfono incorrecta, debe de tener 9 cifras!")

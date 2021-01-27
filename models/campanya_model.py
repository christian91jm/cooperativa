from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date, datetime

class campanya_model(models.Model):
    _name = 'cooperativa.campanya_model'
    _description = 'modelo de campanya'
    
    fecha = fields.Date(string="Fecha", required=True, default=datetime.now())
    campanya = fields.Date(string="Campaña", default= datetime.now().year)
    cantidad = fields.Integer(string="Cantidad")
    id_socio = fields.Many2one("cooperativa.socios_model", string="socio")


    @api.constrains("cantidad")
    def _comprobarCantidad(self):
        if self.cantidad<0:
            raise ValidationError("La cantidad no puede ser negativa!")
    

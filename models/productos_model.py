from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date, datetime

class productos_model(models.Model):
    _name = 'cooperativa.productos_model'
    _description = 'modelo de producto'
    #limitamos name
    _sql_constraints = [('producto_name_uniq','UNIQUE (name)','No puede haber dos productos iguales'),]

    name = fields.Char(string="Nombre", required=True)
    descripcion = fields.Html(string="Descripción", help="Descripción del producto", required=True)
    precio = fields.Float(string="Precio", required=True)
    kilosTotales = fields.Integer(string="Kilos Totales", default=0, readonly=True)



    @api.constrains("precio")
    def _comprobarPrecio(self):
        if len(self.precio)<0:
            raise ValidationError("El precio no puede ser negativo!")
    
    def eliminaKilos(self):
        self.kilosTotales=0
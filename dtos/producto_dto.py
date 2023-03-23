from models.producto_model import Producto
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from dtos.categoria_dto import CategoriaDto
class ProductoDto(SQLAlchemyAutoSchema):
    class Meta:
        include_fk = True
        model = Producto

class MostrarProductoDto(SQLAlchemyAutoSchema):
    categoria = fields.Nested(nested = CategoriaDto)
    class Meta:
        include_fk = True
        load_instance = True
        model = Producto
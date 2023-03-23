from sqlalchemy import Column, types
from sqlalchemy.sql.schema import ForeignKey
from datetime import datetime
from db import connection
from sqlalchemy.orm import relationship
class Producto(connection.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    precio = Column(type_ = types.Float )
    imagen = Column(type_=types.Text)
    categoriaId = Column(ForeignKey(column='categorias.id'), type_=types.Integer, nullable=False, name='categoria_id')

    created_at = Column(type_= types.DateTime, default=datetime.utcnow, name='createdAt')
    categoria = relationship('Categoria', backref = 'productos')
    __tablename__ = 'productos'
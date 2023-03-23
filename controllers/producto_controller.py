from os import path
from flask_restful import Resource, request
from db import connection
from dtos.producto_dto import ProductoDto
from dtos.categoria_dto import CategoriaDto
from dtos.producto_dto import MostrarProductoDto
from models.producto_model import Producto
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
from uuid import uuid4
import os

class ProductoController(Resource):
    def post(self):
        # TODO: validar que tengamos esa llave en el formulario llamada 'imagen'
        # TODO: validar que solo sean imagenes
        # TODO: agregar un uuid al nombre de la imagen y sea un nombre valido
        # TODO: no recibir imagenes que pesen mas de 10Mb
        mimetype_valido = 'image/'

        try:
            data = request.form.to_dict()

            imagen = request.files.get('imagen')
            if imagen is  None:  
                raise Exception("Imagen no presente en el formulario")
            if  mimetype_valido not in imagen.mimetype:
                raise Exception('El archivo no es un archivo valido')
            

            data['imagen'] = imagen.filename
            dto = ProductoDto()
            data_serialized = dto.load(data)
            prod = Producto(**data_serialized)
            connection.session.add(prod)

            nombre_seguro = secure_filename(uuid4().hex + '-' + imagen.filename)
            imagen.save(path.join('images', nombre_seguro))
            connection.session.commit()
            return {
                'message': 'Producto creado'
            }
        except Exception as error:
            connection.session.rollback()
            return {
                'message': 'Error al crear producto',
                'content2': error.description,
                'content': error.args
            }
        
        
    def get(self):
        resultado = connection.session.query(Producto).all()
        dto = MostrarProductoDto()
        data = dto.dump(resultado, many=True)
        return {
            'content': data
        }
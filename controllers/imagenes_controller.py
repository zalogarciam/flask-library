from flask_restful import Resource, request
from flask import send_file
from werkzeug.utils import secure_filename
from os import path
from uuid import uuid4

class ImagenesController(Resource):
    def post(self):

        print(request.form)
        print(request.files)

        imagen = request.files.get('imagen')
        secure_name = secure_filename(uuid4().hex + '-' + imagen.filename)
        imagen.save(path.join('images', secure_name))
        return {
            'message': 'Categoria creada'
        }
    
    def get(self, nombre):
        try:
            return send_file(path.join('images', nombre))
        except FileNotFoundError:
            return send_file(path.join('images', 'not-found.png'))

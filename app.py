from controllers.imagenes_controller import ImagenesController
from flask import Flask
from dotenv import load_dotenv
from os import environ
from flask_migrate import Migrate
from flask_restful import Api

from db import connection
from controllers.categoria_controller import CategoriasController

from utils.enviar_correo import enviar_correo_adjuntos
from controllers.usuario_controller import RegistroController
from controllers.producto_controller import ProductoController

load_dotenv() 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

flask_api = Api(app=app)

connection.init_app(app)


Migrate(app=app, db=connection)

@app.route('/prueba')
def enviar_correo_prueba():
    enviar_correo_adjuntos('gegarciam95@gmail.com', 'Correo con imagenes')
    return {
        'message': 'Correo enviado exitosamente'
    }

@app.errorhandler(413)
def request_entity_too_large(error):
    return 'File Too Large', 413

flask_api.add_resource(RegistroController, '/registro')
flask_api.add_resource(ImagenesController, '/imagenes', '/imagenes/<nombre>')
flask_api.add_resource(CategoriasController, '/categorias')
flask_api.add_resource(ProductoController, '/productos')

if __name__ == '__main__':
    app.run(debug=True)
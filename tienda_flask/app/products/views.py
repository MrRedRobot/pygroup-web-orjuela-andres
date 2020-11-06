from flask import Blueprint

prod = Blueprint('prod', __name__, url_prefix='/products')

@prod.route('/<name>', methods=['GET'])
def get_products(name):
     stn = "<h1>Bienvenido a productos</h1><br/><br/>"
     stn = stn + "Mostrando sitio del producto {}".format(name)
     return stn

def render_template():
    return None
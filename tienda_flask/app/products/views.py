from flask import Blueprint

prod = Blueprint('prod', __name__, url_prefix='/products')

@prod.route('/<name>', methods=['GET'])
def get_products(name):
     stn = "<h1>Bienvenido a productos</h1><br/><br/>"
     stn = stn + "Mostrando sitio del producto {}".format(name)
     return stn

def render_template():
    return None

#Flask proporciona una función llamada render_template()para renderizar Plantillas. Es esta función la que integra Jinja con Flask. 
#Para renderizar una plantilla, llamamos render_template()con el nombre de la plantilla junto con los datos que desea pasar a la plantilla como argumentos de palabras clave. La render_template()función representa la plantilla y devuelve HTML como una cadena. 
#Los argumentos de palabras clave que pasamos a la plantilla se conocen como contexto de la plantilla o simplemente contexto de plantilla.

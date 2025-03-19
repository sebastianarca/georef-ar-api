# flake8: noqa: F401
# pylint: disable=wrong-import-position
"""Módulo '__init__' de georef-ar-api

Crea la aplicación Flask de la API de Georef.
"""
import os
from flask import Flask

app = Flask('georef', static_folder=None)
app.config.from_envvar('GEOREF_CONFIG')
app.config['ES_HOSTS'] = os.getenv('ES_HOSTS', app.config.get('ES_HOSTS', ['localhost']))

with app.app_context():
    # Crear parsers de parámetros utilizando configuración de Flask app
    import service.params
    # Crear rutas utilizando también configuración de Flask
    import service.routes

    from service import utils
    utils.patch_json_encoder(app)


def georef_console():
    """Inicia una consola interactiva de Python con algunos módulos de
    georef-ar-api precargados para realizar pruebas rápidas.

    """
    import code
    with app.app_context():
        console = code.InteractiveConsole(locals=locals())
        console.push('import service')
        console.push('es = service.normalizer.get_elasticsearch()')
        console.interact()

#def apptest(environ, start_response):
#    status = '200 OK'
#    output = 'Hello World from within the hiv app, after all that!'
#
#    response_headers = [('Content-type', 'text/plain'),
#                        ('Content-Length', str(len(output)))]
#
#    start_response(status, response_headers)
#
#    return [output]
from flask import Flask
import backbone


# TODO: fix static folder, this requires adapting HTML templates
hiv = Flask(__name__)
hiv.config.from_object('config')
hiv.config['SECTIONS'] = backbone.sections
hiv.config['DATA_SUBFOLDER'] = 'data'

from .blueprints.tutorial import tutorial
hiv.register_blueprint(tutorial, url_prefix='/tutorial')

from .blueprints.welcome import welcome
hiv.register_blueprint(welcome, url_prefix='/welcome')

from .blueprints.patient import patient
hiv.register_blueprint(patient, url_prefix='/patient')


from . import views


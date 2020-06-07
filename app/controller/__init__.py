from flask_restplus import Api

from app.controller.demo import api as demo_api

api = Api(
    title='Software Testing Visual Platform',
    version='1.0',
    description='Software Testing Visual Platform'
)

api.add_namespace(demo_api, path='/demo')

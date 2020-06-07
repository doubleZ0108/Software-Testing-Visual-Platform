from flask_restplus import Namespace, Resource, fields
from app.model.demo import model
from app.service.demo import demo as demo_service

api = Namespace('demo_namespace', description='Demo Namespace')
model = api.model('Demo Model', model)


@api.route('/')
class DemoModelList(Resource):
    @api.doc('list_demo_models')
    @api.marshal_list_with(model)
    def get(self):
        """
        List all demo models
        """
        return demo_service.get_all()

    @api.doc('create demo model')
    @api.expect(model)
    @api.marshal_with(model, code=201)
    def post(self):
        """
        create a new model
        """
        return demo_service.create_model(api.payload), 201


@api.route('/<id>')
@api.param('id', 'The model identifier')
@api.response(404, 'Model not found')
class Cat(Resource):
    @api.doc('get_model')
    @api.marshal_with(model)
    def get(self, id):
        """Fetch a model given its identifier"""
        result = demo_service.get_by_id(id)
        if result is None:
            api.abort(404)
        return result

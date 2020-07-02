from flask_restplus import Namespace, Resource, fields
from app.model.question7 import model
from app.service.question7 import question7 as question7_service

api = Namespace('question7', description='电信收费问题')
model = api.model('Commission', model=model)


@api.route('/charge/<method_type>')
@api.param('method_type', 'boundary | equivalence | decision | final')
@api.response(404, 'Method not found')
class Calendar(Resource):
    @api.doc('Charge Problem')
    def get(self, method_type):
        """
        电信收费问题
        """
        return question7_service.charge(method_type)


@api.route('/charge/')
class CalenderBasic(Resource):
    @api.doc('Charge Problem Basic Method')
    @api.expect(model)
    def post(self):
        """
        电信收费问题的基础实现
        """
        return question7_service.charge_method_test(api.payload)


@api.route('/charge/<code_version>')
@api.param('code_version', 'v1 | v2')
class CalenderBasic(Resource):
    @api.doc('Charge Problem Basic Method')
    @api.expect(model)
    def post(self, code_version):
        """
        版本-电信收费问题的基础实现
        """
        return question7_service.charge_method_test(api.payload, code_version)


@api.route('/charge/<method_type>/<code_version>')
@api.param('method_type', 'boundary | equivalence | decision')
@api.param('code_version', 'v1 | v2')
@api.response(404, 'Method not found')
class Calendar(Resource):
    @api.doc('Charge Problem')
    def get(self, method_type, code_version):
        """
        版本-电信收费问题
        """
        return question7_service.charge(method_type, code_version)

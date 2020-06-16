from flask_restplus import Namespace, Resource, fields
from app.model.question2 import model
from app.service.question2 import question2 as question2_service

api = Namespace('question2', description='佣金问题')
model = api.model('Comission', model=model)


@api.route('/commission/<method_type>')
@api.param('method_type', 'boundary')
@api.response(404, 'Method not found')
class Calendar(Resource):
    @api.doc('Commission Problem')
    def get(self, method_type):
        """
        佣金问题
        """
        return question2_service.commission(method_type)


@api.route('/commission/')
class CalenderBasic(Resource):
    @api.doc('Commission Problem Basic Method')
    @api.expect(model)
    def post(self):
        """
        佣金问题的基础实现
        """
        return question2_service.commission_method_test(api.payload)

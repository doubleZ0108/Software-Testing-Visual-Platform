from flask_restplus import Namespace, Resource, fields
from app.model.question8 import model
from app.service.question8 import question8 as question8_service

api = Namespace('question8', description='销售系统问题')
model = api.model('Sales', model)

@api.route('/sales/<method_type>')
@api.param('method_type', 'statement | judge | condition | judge-condition | condition-combination')
@api.response(404, 'Method not found')
class Sales(Resource):
    @api.doc('Sales Problem')
    def get(self, method_type):
        """
        销售系统问题
        """
        return question8_service.sales(method_type)



@api.route('/sales/')
class SalesBase(Resource):
    @api.doc('Sales Problem Basic Method')
    @api.expect(model)
    def post(self):
        """
        销售系统问题的基础实现
        """
        return question8_service.sales_method_test(api.payload)

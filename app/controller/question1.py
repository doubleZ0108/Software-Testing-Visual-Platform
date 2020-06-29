from flask_restplus import Namespace, Resource, fields
from app.model.question1 import triangle_model as q1_model
from app.model.question1 import calender_model as q2_model
from app.service.question1 import question1 as question1_service

api = Namespace('question1', description='三角形/万年历问题')
q1_model = api.model('Triangle', model=q1_model)
q2_model = api.model('Calender', model=q2_model)


@api.route('/triangle/<method_type>')
@api.param('method_type', 'boundary | equivalence')
@api.response(404, 'Method not found')
class Triangle(Resource):
    @api.doc('Triangle Problem')
    def get(self, method_type):
        """
        三角形问题
        """
        return question1_service.triangle(method_type)


@api.route('/triangle/<method_type>/<code_version>')
@api.param('method_type', 'boundary | equivalence')
@api.param('code_version', 'v1 | v2')
@api.response(404, 'Method not found')
class Triangle(Resource):
    @api.doc('Triangle Problem')
    def get(self, method_type, code_version):
        """
        版本-三角形问题
        """
        return question1_service.triangle(method_type, code_version)


@api.route('/calendar/<method_type>')
@api.param('method_type',
           'boundary | equivalence-weak-general ｜ equivalence-strong-general ｜ equivalence-weak-robust ｜ equivalence-strong-robust')
@api.response(404, 'Method not found')
class Calendar(Resource):
    @api.doc('Calendar Problem')
    def get(self, method_type):
        """
        万年历问题
        """
        return question1_service.calendar(method_type)


@api.route('/triangle/')
class TriangleBasic(Resource):
    @api.doc('Triangle Problem Basic Method')
    @api.expect(q1_model)
    def post(self):
        """
        三角形问题的基础实现
        """
        return question1_service.triangle_method_test(api.payload)


@api.route('/triangle/<code_version>')
@api.param('code_version', 'v1 | v2')
class TriangleBasic(Resource):
    @api.doc('Triangle Problem Basic Method')
    @api.expect(q1_model)
    def post(self, code_version):
        """
        版本-三角形问题的基础实现
        """
        return question1_service.triangle_method_test(api.payload, code_version)


@api.route('/calendar/')
class CalenderBasic(Resource):
    @api.doc('Calender Problem Basic Method')
    @api.expect(q2_model)
    def post(self):
        """
        万年历问题的基础实现
        """
        return question1_service.calendar_method_test(api.payload)

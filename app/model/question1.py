from flask_restplus import fields

triangle_model = {
    'edge1': fields.Float(required=True, description='边1'),
    'edge2': fields.Float(required=True, description='边2'),
    'edge3': fields.Float(required=True, description='边3')
}
calender_model = {
    'year': fields.Integer(required=True, description='年'),
    'month': fields.Integer(required=True, description='月'),
    'day': fields.Integer(required=True, description='日')
}
MODELS = []

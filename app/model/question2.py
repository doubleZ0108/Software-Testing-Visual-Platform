from flask_restplus import fields

model = {
    'host': fields.Integer(required=True, description='主机数目'),
    'display': fields.Integer(required=True, description='显示器数目'),
    'peripheral': fields.Integer(required=True, description='外设数目')
}

MODELS = []

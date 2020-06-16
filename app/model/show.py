from flask_restplus import fields

model = {
    'problem': fields.String(required=True, description='问题名称'),
    'method_type': fields.String(required=True, description='方法类型'),
}

MODELS = []

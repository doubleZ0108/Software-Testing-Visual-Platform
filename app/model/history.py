from flask_restplus import fields

history = {
    'method_type': fields.String(required=True, description='测试方法'),
    'code_version': fields.String(required=True, description='代码版本')
}

MODELS = []

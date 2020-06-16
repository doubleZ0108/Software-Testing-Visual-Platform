from flask_restplus import fields

model = {
    'id': fields.String(required=True, description='Model Identifier'),
    'content': fields.String(required=True, description='Model Content'),
}


MODELS = [
    {'id': '1', 'content': 'content1'}
]


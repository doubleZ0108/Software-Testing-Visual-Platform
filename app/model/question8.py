from flask_restplus import fields

model = {
    'annual_sales': fields.Float(required=True, description='年销售额(万元)'),
    'leave_days': fields.Integer(required=True, description='请假天数(天)'),
    'rate_cash_to_account': fields.Float(required=True, description='现金到帐率(0.x)'),
}

MODELS = []

from flask_restplus import fields

model = {
    'talk_time_month': fields.Integer(required=True, description='当月通话时间'),
    'unpaid_num_year': fields.Integer(required=True, description='年度累计未按时缴费的次数'),
    'unpaid_cost_across_year': fields.Float(required=True, description='跨年未缴费费用'),
    'pay_method': fields.String(required=True, description='支付方式')
}

MODELS = []

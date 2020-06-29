from flask_restplus import Api

from app.controller.demo import api as demo_api
from app.controller.question1 import api as question1_api
from app.controller.question2 import api as question2_api
from app.controller.question7 import api as question7_api
from app.controller.question6 import api as question6_api
from app.controller.question8 import api as question8_api
from app.controller.show import api as show_csv_api
api = Api(
    title='Software Testing Visual Platform',
    version='v1.0',
    description='Software Testing Visual Platform Api'
)

api.add_namespace(demo_api, path='/demo')
api.add_namespace(question1_api, path='/question1')
api.add_namespace(question2_api, path='/question2')
api.add_namespace(question7_api, path='/question7')
api.add_namespace(question6_api, path='/question6')
api.add_namespace(question8_api, path='/question8')
api.add_namespace(show_csv_api, path='/show-csv')

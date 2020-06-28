from flask_restplus import Namespace, Resource, fields
from app.model.show import model
from app.service.show import ShowCSV
import flask

api = Namespace('show_csv', description='csv展示')
model = api.model('Show', model=model)


@api.route('/')
class CalenderBasic(Resource):
    @api.doc('Display CSV Table')
    @api.expect(model)
    def post(self):
        """
        展示CSV表格
        """
        return ShowCSV.get_csv(api.payload)

    @api.doc('Get Problem Item')
    def get(self):
        """
        获得问题项目
        """
        return ShowCSV.get_csv_dir()

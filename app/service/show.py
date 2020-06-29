from app.csv.index import csv_dir2
from app.csv.index import csv_dir
import pandas as pd
import json
from collections import OrderedDict


class ShowCSV:
    @staticmethod
    def get_csv(request):
        problem, method_type = request['problem'], request['method_type']
        df = pd.read_csv(csv_dir2[problem][method_type])
        temp_json = df.to_json(orient='records')
        temp_dict = json.loads(temp_json, object_pairs_hook=OrderedDict)
        return temp_dict

    @staticmethod
    def get_csv_dir():
        return csv_dir

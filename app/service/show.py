from app.csv.index import csv_dir
import pandas as pd
import json
from collections import OrderedDict


class ShowCSV:
    @staticmethod
    def get_csv(request):
        problem, method_type = request['problem'], request['method_type']
        df = pd.read_csv(csv_dir[problem][method_type])
        temp_json = df.to_json(orient='records')
        # print(temp_json)
        temp_dict = json.loads(temp_json, object_pairs_hook=OrderedDict)
        print(temp_dict)
        return temp_dict

    @staticmethod
    def get_csv_dir():
        return csv_dir

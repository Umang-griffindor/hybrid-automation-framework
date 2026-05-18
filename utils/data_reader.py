import json


class DataReader:

    @staticmethod
    def read_json_data(file_path):

        with open(file_path) as file:

            return json.load(file)
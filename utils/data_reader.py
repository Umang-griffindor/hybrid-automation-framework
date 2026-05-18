import json  # Python import for reading test data stored as JSON


class DataReader:  # Python class for data-driven testing helpers

    @staticmethod  # static method since no state is needed to read JSON files
    def read_json_data(file_path):  # method reads test data from a given file path

        with open(file_path) as file:  # Python file open inside a safe context manager

            return json.load(file)  # parse JSON content into Python data structures
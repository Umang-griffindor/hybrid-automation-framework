import json  # Python import for JSON parsing of config files
import os  # Python import for reading environment variables and constructing file paths


class ConfigReader:  # Python class providing configuration loading utilities

    @staticmethod  # static method syntax because no object instance is required
    def read_config():  # method reads environment-specific JSON config into a Python dict

        environment = os.getenv(
            "TEST_ENV",
            "qa"
        )  # read TEST_ENV from environment or default to QA environment

        print(
            f"\nRunning tests on environment: "
            f"{environment.upper()}"
        )  # print environment information to help debug which config is used

        config_path = (
            f"configs/{environment}_config.json"
        )  # build the path to the selected environment config file

        with open(config_path) as config_file:  # open the config file safely with a context manager

            return json.load(config_file)  # parse JSON from the file into a Python dictionary
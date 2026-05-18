import json
import os


class ConfigReader:

    @staticmethod
    def read_config():

        environment = os.getenv(
            "TEST_ENV",
            "qa"
        )

        print(
            f"\nRunning tests on environment: "
            f"{environment.upper()}"
        )

        config_path = (
            f"configs/{environment}_config.json"
        )

        with open(config_path) as config_file:

            return json.load(config_file)
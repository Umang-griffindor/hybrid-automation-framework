import os
from datetime import datetime


def generate_screenshot_path(test_name):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    screenshots_dir = "screenshots"


    if not os.path.exists(screenshots_dir):

        os.makedirs(screenshots_dir)


    return f"{screenshots_dir}/{test_name}_{timestamp}.png"
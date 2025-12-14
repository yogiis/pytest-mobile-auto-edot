import os
import random
import string
from datetime import datetime


def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_random_email():
    random_str = generate_random_string(8).lower()
    return f"test_{random_str}@example.com"


def take_screenshot_with_timestamp(driver, name, directory="reports/screenshots"):
    os.makedirs(directory, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{timestamp}.png"
    filepath = os.path.join(directory, filename)
    driver.save_screenshot(filepath)
    return filepath

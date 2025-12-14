"""
Allure helper utilities for enhanced reporting.
"""
import allure
from functools import wraps


def allure_step(step_name):
    """Decorator to wrap a method as an Allure step."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with allure.step(step_name):
                return func(*args, **kwargs)
        return wrapper
    return decorator


def attach_screenshot(driver, name="screenshot"):
    """Attach screenshot to Allure report."""
    allure.attach(
        driver.get_screenshot_as_png(),
        name=name,
        attachment_type=allure.attachment_type.PNG
    )


def attach_page_source(driver, name="page_source"):
    """Attach page source to Allure report."""
    allure.attach(
        driver.page_source,
        name=name,
        attachment_type=allure.attachment_type.XML
    )


def attach_text(text, name="text"):
    """Attach text to Allure report."""
    allure.attach(
        text,
        name=name,
        attachment_type=allure.attachment_type.TEXT
    )


def attach_json(json_content, name="json"):
    """Attach JSON to Allure report."""
    import json
    allure.attach(
        json.dumps(json_content, indent=2),
        name=name,
        attachment_type=allure.attachment_type.JSON
    )

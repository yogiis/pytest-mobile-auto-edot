import pytest
import allure
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.config import Config


@pytest.fixture(scope="session")
def config():
    return Config()


@pytest.fixture(scope="function")
def driver(config, request):
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = config.ANDROID_DEVICE_NAME
    options.automation_name = "UiAutomator2"
    options.app_package = config.ANDROID_APP_PACKAGE
    options.app_activity = config.ANDROID_APP_ACTIVITY
    options.no_reset = True
    
    driver = webdriver.Remote(
        command_executor=config.APPIUM_SERVER_URL,
        options=options
    )
    driver.implicitly_wait(config.IMPLICIT_WAIT)
    
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
    
    if rep.when == "call" and rep.failed:
        try:
            driver = item.funcargs.get("driver")
            if driver:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="screenshot_on_failure",
                    attachment_type=allure.attachment_type.PNG
                )
        except Exception:
            pass

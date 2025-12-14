import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from config.config import Config


@pytest.fixture(scope="session")
def config():
    return Config()


@pytest.fixture(scope="function")
def driver(config):
    options = ChromeOptions()
    if config.HEADLESS:
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    
    driver.implicitly_wait(config.IMPLICIT_WAIT)
    
    if config.MAXIMIZE_WINDOW:
        driver.maximize_window()
    
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
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

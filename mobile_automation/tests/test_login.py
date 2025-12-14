import pytest
import allure
from pages.login_page import LoginPage
from config.config import Config


@allure.epic("EDOT eWork Mobile App")
@allure.feature("Authentication")
class TestLogin:
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.config = Config()
    
    @allure.title("Login with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_success(self):
        with allure.step("Verify login page displayed"):
            assert self.login_page.is_login_page_displayed()
        
        with allure.step("Login with valid credentials"):
            self.login_page.login(
                company_id=self.config.TEST_COMPANY_ID,
                username=self.config.TEST_USERNAME,
                password=self.config.TEST_PASSWORD
            )
        
        with allure.step("Verify login successful"):
            assert not self.login_page.is_login_page_displayed()

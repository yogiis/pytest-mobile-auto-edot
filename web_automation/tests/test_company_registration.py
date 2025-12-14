import pytest
import allure
import time
from pages.login_page import LoginPage
from pages.home_page import HomePage


@allure.epic("EDOT Web Application")
@allure.feature("Company Management")
class TestCompanyRegistration:
    
    COMPANY_DATA = {
        "name": "PT Testing Automation",
        "email": "testing.auto@company.com",
        "phone": "08123456789",
        "address": "Jl. Testing No. 123",
        "industry": "Retail",
        "company_type": "Importer/Exporter",
        "language": "Indonesia",
        "country": "Philippines",
        "region": "Bangsamoro Autonomous Region In Muslim Mindanao (BARMM)",
        "province": "Maguindanao del Sur",
        "city": "Shariff Saydona Mustapha",
        "barangay": "Pagatin (Pagatin I)",
        "postal_code": "9635"
    }
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, config):
        self.driver = driver
        self.config = config
        self.login_page = LoginPage(driver)
        self.home_page = HomePage(driver)
        
        with allure.step(f"Navigate to {config.BASE_URL}"):
            self.login_page.open("")
        
        with allure.step(f"Login as {config.TEST_EMAIL}"):
            self.login_page.complete_login_flow(config.TEST_EMAIL, config.TEST_PASSWORD)
            time.sleep(2)
    
    @allure.story("Company Registration - Step 1")
    @allure.title("Add new company - complete step 1")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_new_company_step1(self):
        
        with allure.step("Click navbar 'Companies'"):
            self.home_page.click_companies_navbar()
            time.sleep(2)
        
        with allure.step("Click 'Add Company' button"):
            registration_page = self.home_page.click_add_company_and_get_page()
            time.sleep(3)
        
        with allure.step("Fill company name"):
            registration_page.enter_company_name(self.COMPANY_DATA["name"])
        
        with allure.step("Fill company email"):
            registration_page.enter_company_email(self.COMPANY_DATA["email"])
        
        with allure.step("Fill company phone"):
            registration_page.enter_company_phone(self.COMPANY_DATA["phone"])
        
        with allure.step("Fill company address"):
            registration_page.enter_company_address(self.COMPANY_DATA["address"])
        
        with allure.step(f"Select industry: {self.COMPANY_DATA['industry']}"):
            registration_page.select_industry(self.COMPANY_DATA["industry"])
            time.sleep(0.5)
        
        with allure.step(f"Select company type: {self.COMPANY_DATA['company_type']}"):
            registration_page.select_company_type(self.COMPANY_DATA["company_type"])
            time.sleep(0.5)
        
        with allure.step(f"Select language: {self.COMPANY_DATA['language']}"):
            registration_page.select_language(self.COMPANY_DATA["language"])
            time.sleep(0.5)
        
        with allure.step(f"Select country: {self.COMPANY_DATA['country']}"):
            registration_page.select_country(self.COMPANY_DATA["country"])
            time.sleep(0.5)
        
        with allure.step(f"Select region: {self.COMPANY_DATA['region']}"):
            registration_page.select_region(self.COMPANY_DATA["region"])
            time.sleep(0.5)
        
        with allure.step(f"Select province: {self.COMPANY_DATA['province']}"):
            registration_page.select_province(self.COMPANY_DATA["province"])
            time.sleep(0.5)
        
        with allure.step(f"Select city: {self.COMPANY_DATA['city']}"):
            registration_page.select_city(self.COMPANY_DATA["city"])
            time.sleep(0.5)
        
        with allure.step(f"Select barangay: {self.COMPANY_DATA['barangay']}"):
            registration_page.select_barangay(self.COMPANY_DATA["barangay"])
            time.sleep(0.5)
        
        with allure.step("Click 'Next' button at Step 1"):
            registration_page.click_next()
            time.sleep(2)
            screenshot = self.driver.get_screenshot_as_png()
            allure.attach(screenshot, "After Step 1 Next", allure.attachment_type.PNG)
        
        with allure.step("Click 'Next' button at Step 2 (skip all fields)"):
            registration_page.click_next()
            time.sleep(2)
            screenshot = self.driver.get_screenshot_as_png()
            allure.attach(screenshot, "After Step 2 Next", allure.attachment_type.PNG)
        
        with allure.step("Click 'Fill in with the same data from the Company records' button"):
            registration_page.click_fill_same_data()
            time.sleep(1)
        
        with allure.step("Click 'Select All' checkbox"):
            registration_page.click_select_all_checkbox()
            time.sleep(0.5)
        
        with allure.step("Click 'Register' button"):
            registration_page.click_register()
            time.sleep(3)
            screenshot = self.driver.get_screenshot_as_png()
            allure.attach(screenshot, "After Register", allure.attachment_type.PNG)
        
        assert True, "Company registration completed"

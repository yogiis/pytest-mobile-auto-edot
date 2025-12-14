from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    
    COMPANIES_NAVBAR_LINK = (By.XPATH, "//a[@href='/companies' and contains(., 'Companies')]")
    ADD_COMPANY_BUTTON = (By.XPATH, "//button[contains(., 'Add Company')]")
    
    def click_companies_navbar(self):
        self.click(self.COMPANIES_NAVBAR_LINK)

    def click_add_company_and_get_page(self):
        self.click(self.ADD_COMPANY_BUTTON)
        from pages.company_registration_page import CompanyRegistrationPage
        return CompanyRegistrationPage(self.driver)

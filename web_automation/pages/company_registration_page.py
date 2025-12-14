from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CompanyRegistrationPage(BasePage):
    
    COMPANY_NAME_INPUT = (By.XPATH, "//input[@placeholder='Input Company Name']")
    COMPANY_EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Input Email']")
    COMPANY_PHONE_INPUT = (By.XPATH, "//input[@placeholder='Input Phone']")
    COMPANY_ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='Input Address']")
    
    INDUSTRY_TYPE_SELECT = (By.XPATH, "//span[normalize-space()='Choose Industry Type']/ancestor::button")
    COMPANY_TYPE_SELECT = (By.XPATH, "//span[normalize-space()='Choose Company Type']/ancestor::button")
    CHOOSE_LANGUAGE_SELECT = (By.XPATH, "//span[normalize-space()='Choose Language']/ancestor::button")
    
    COUNTRY_SELECT = (By.XPATH, "//span[normalize-space()='Choose Country']/ancestor::button")
    REGION_SELECT = (By.XPATH, "//span[normalize-space()='Choose Region']/ancestor::button")
    PROVINCE_SELECT = (By.XPATH, "//span[normalize-space()='Choose Province']/ancestor::button")
    CITY_SELECT = (By.XPATH, "//span[normalize-space()='Choose City']/ancestor::button")
    BARANGAY_SELECT = (By.XPATH, "//span[normalize-space()='Choose Barangay']/ancestor::button")
    POSTAL_CODE_SELECT = (By.XPATH, "//span[normalize-space()='Choose Postal Code']/ancestor::button")
    
    NEXT_BUTTON = (By.XPATH, "//button[normalize-space()='Next']")
    
    FILL_SAME_DATA_BUTTON = (By.XPATH, "//button[contains(., 'Fill in with the same data from the Company records')]")
    SELECT_ALL_CHECKBOX = (By.ID, "select-all")
    REGISTER_BUTTON = (By.XPATH, "//button[normalize-space()='Register']")
    
    def option_by_text(self, text: str):
        return (By.XPATH, f"//div[@role='option' and (contains(., '{text}') or .//span[normalize-space()='{text}'])]")
    
    def enter_company_name(self, name: str):
        self.send_keys(self.COMPANY_NAME_INPUT, name)
    
    def enter_company_email(self, email: str):
        self.send_keys(self.COMPANY_EMAIL_INPUT, email)
    
    def enter_company_phone(self, phone: str):
        self.send_keys(self.COMPANY_PHONE_INPUT, phone)
    
    def enter_company_address(self, address: str):
        self.send_keys(self.COMPANY_ADDRESS_INPUT, address)
    
    def select_industry(self, industry_text: str):
        self.click(self.INDUSTRY_TYPE_SELECT)
        self.click(self.option_by_text(industry_text))
    
    def select_company_type(self, company_type_text: str):
        self.click(self.COMPANY_TYPE_SELECT)
        self.click(self.option_by_text(company_type_text))
    
    def select_language(self, language_text: str):
        from selenium.webdriver.common.keys import Keys
        self.click(self.CHOOSE_LANGUAGE_SELECT)
        option = self.option_by_text(language_text)
        self.click(option)
        import time
        time.sleep(0.5)
    
    def select_country(self, country_name: str):
        self.click(self.COUNTRY_SELECT)
        self.click(self.option_by_text(country_name))
    
    def select_region(self, region_name: str):
        self.click(self.REGION_SELECT)
        self.click(self.option_by_text(region_name))
    
    def select_province(self, province_name: str):
        self.click(self.PROVINCE_SELECT)
        self.click(self.option_by_text(province_name))
    
    def select_city(self, city_name: str):
        self.click(self.CITY_SELECT)
        self.click(self.option_by_text(city_name))
    
    def select_barangay(self, barangay_name: str):
        self.click(self.BARANGAY_SELECT)
        self.click(self.option_by_text(barangay_name))
    
    def select_postal_code(self, postal_code: str):
        self.click(self.POSTAL_CODE_SELECT)
        self.click(self.option_by_text(postal_code))
    
    def click_next(self):
        self.click(self.NEXT_BUTTON)
    
    def click_fill_same_data(self):
        self.click(self.FILL_SAME_DATA_BUTTON)
    
    def click_select_all_checkbox(self):
        self.click(self.SELECT_ALL_CHECKBOX)
    
    def click_register(self):
        self.click(self.REGISTER_BUTTON)

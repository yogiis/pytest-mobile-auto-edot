from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class LoginPage(BasePage):
    
    COMPANY_ID_INPUT = (AppiumBy.ID, "id.edot.ework:id/tv_company_id")
    USERNAME_INPUT = (AppiumBy.ID, "id.edot.ework:id/tv_username")
    PASSWORD_INPUT = (AppiumBy.ID, "id.edot.ework:id/tv_password")
    LOGIN_BUTTON = (AppiumBy.ID, "id.edot.ework:id/button_text")
    
    def enter_company_id(self, company_id):
        self.send_keys(self.COMPANY_ID_INPUT, company_id)
    
    def enter_username(self, username):
        self.send_keys(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        self.send_keys(self.PASSWORD_INPUT, password)
    
    def click_login(self):
        self.click(self.LOGIN_BUTTON)
    
    def login(self, company_id, username, password):
        self.enter_company_id(company_id)
        self.enter_username(username)
        self.enter_password(password)
        self.hide_keyboard()
        self.click_login()
    
    def is_login_page_displayed(self):
        return self.is_element_visible(self.COMPANY_ID_INPUT)

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    
    EMAIL_USERNAME_BUTTON = (By.XPATH, "//button[contains(text(), 'Use Email or Username')]")
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Log In')]")
    
    def click_email_username_button(self):
        self.click(self.EMAIL_USERNAME_BUTTON)
    
    def enter_email_or_username(self, email_or_username):
        self.send_keys(self.USERNAME_INPUT, email_or_username)
    
    def click_login_submit(self):
        self.click(self.LOGIN_SUBMIT_BUTTON)
    
    def enter_password(self, password):
        import time
        time.sleep(1)
        self.send_keys(self.PASSWORD_INPUT, password)
    
    def complete_login_flow(self, email, password):
        self.click_email_username_button()
        self.enter_email_or_username(email)
        self.click_login_submit()
        self.enter_password(password)
        self.click_login_submit()

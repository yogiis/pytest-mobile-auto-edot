from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from config.config import Config


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.config = Config()
        self.wait = WebDriverWait(driver, self.config.EXPLICIT_WAIT)
    
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def is_element_visible(self, locator, timeout=None):
        try:
            wait = WebDriverWait(self.driver, timeout or self.config.EXPLICIT_WAIT)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
    
    def hide_keyboard(self):
        try:
            self.driver.hide_keyboard()
        except:
            pass

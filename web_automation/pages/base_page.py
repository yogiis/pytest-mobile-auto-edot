from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from config.config import Config


class BasePage:
    """Simplified base page with only essential methods for our test flow."""
    
    def __init__(self, driver):
        self.driver = driver
        self.config = Config()
        self.wait = WebDriverWait(driver, self.config.EXPLICIT_WAIT)
    
    # ==================== Navigation ====================
    
    def open(self, path=""):
        """Open URL with base URL + path."""
        self.driver.get(f"{self.config.BASE_URL}{path}")
    
    # ==================== Element Actions ====================
    
    def find_element(self, locator):
        """Find element with explicit wait."""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click(self, locator):
        """Click element with wait for clickable and scroll into view."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)
    
    def send_keys(self, locator, text):
        """Clear and type text into element."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def is_element_visible(self, locator, timeout=None):
        """Check if element is visible."""
        try:
            wait = WebDriverWait(self.driver, timeout or self.config.EXPLICIT_WAIT)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

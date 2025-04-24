from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self,*locator):
        return self.driver.find_element(*locator)

    def input_text(self,text,*locator):
        self.driver.find_element(*locator).send_keys(text)

    def click(self,*locator):
        self.driver.find_element(*locator).click()

    def wait_and_click(self,locator):
        self.wait.until(EC.visibility_of_element_located(locator),message=f'Element by {locator} not clickable').click()


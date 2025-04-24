from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class SideNavigationPage(BasePage):
    MARKET = (By.XPATH, "//input[@class='g-menu-text']")

    def click_market_button(self):
        self.wait_and_click(self.MARKET)
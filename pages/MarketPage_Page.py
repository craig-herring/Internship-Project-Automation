from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class MarketPage_Page(BasePage):

    click_market_button = (By.XPATH, "//input[@class='g-menu-text']")


 #   def verify_market_url(self):
 #       self.verify_url("https://soft.reelly.io/market")

from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.SideNavigation_Page import SideNavigationPage
from pages.MarketPage_Page import MarketPage_Page


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.BasePage = BasePage(driver)
        self.LoginPage = LoginPage(driver)
        self.SideNavigationPage = SideNavigationPage(driver)
        self.MarketPage_Page = MarketPage_Page(driver)
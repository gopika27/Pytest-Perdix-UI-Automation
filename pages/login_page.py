import logging
from playwright.sync_api import Page
from pages.base_page import BasePage
import allure

logger = logging.getLogger(__name__)

class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.account_number = "#account-number"
        self.username = "#username"
        self.password = "#password"
        self.login_btn = "button:has-text('login')"
        
    @allure.step("Open login page")
    def load(self):
        logger.info("Navigating to login page")
        self.page.goto("https://staging.perdixdigital.com/auth/login", timeout=60000)
        
    @allure.step("Login with account number")
    def login(self, acc, user, pwd):
        logger.info("Entering login details")
        self.fill(self.account_number, acc)
        self.fill(self.username, user)
        self.fill(self.password, pwd)

        logger.info("Clicking login button")
        self.click(self.login_btn)
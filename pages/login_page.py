import os
import time
from constants.config import config
from pages.base_page import BasePage
from locators.locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def __init__(self, driver):
        self.url = os.path.join(config.BASE_URL, 'login')
        self.locator = LoginPageLocators
        super().__init__(driver)

    def go_to_login_page(self):
        self.go_to_page(self.url)

    def set_user_inputs(self, username, password):
        self.driver.find_element(*LoginPageLocators.username_input).send_keys(username)
        time.sleep(0.5)
        self.driver.find_element(*LoginPageLocators.password_input).send_keys(password)
        time.sleep(0.5)
        self.driver.find_element(*LoginPageLocators.login_button).click()
        # time.sleep(0.5)
        # self.driver.find_element(*LoginPageLocators.profile).click()
        # time.sleep(0.5)
        # self.driver.find_element(*LoginPageLocators.logout_link).click()
        time.sleep(1)


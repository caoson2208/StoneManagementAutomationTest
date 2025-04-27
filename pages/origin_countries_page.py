import os
import time
from constants.config import config
from pages.base_page import BasePage
from locators.locators import OriginCountriesPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class OriginCountriesPage(BasePage):

    def __init__(self, driver):
        self.url = os.path.join(config.BASE_URL, 'c-origin-countries')
        self.locator = OriginCountriesPageLocators
        super().__init__(driver)

    def go_to_origin_countries_page(self):
        self.go_to_page(self.url)

    def click_and_wait(self, locator, clear=False, keys=None):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        if clear:
            element.clear()
        if keys:
            element.send_keys(keys)
        else:
            element.click()
        time.sleep(0.5)    

    def new_origin_countries(self):
        time.sleep(0.5)
        self.click_and_wait(self.locator.new_origin_country_button)
        self.click_and_wait(self.locator.origin_country_combobox)
        self.click_and_wait(self.locator.origin_country_option)
        self.click_and_wait(self.locator.save_button)
        time.sleep(0.5)

    def edit_origin_countries(self):
        self.click_and_wait(self.locator.edit_button)
        self.click_and_wait(self.locator.origin_country_combobox)
        self.click_and_wait(self.locator.origin_country_option)
        self.click_and_wait(self.locator.save_button)
        time.sleep(0.5)

    def delete_origin_countries(self):
        self.click_and_wait(self.locator.delete_button)
        self.click_and_wait(self.locator.cancel_button)
        self.click_and_wait(self.locator.delete_button)
        self.click_and_wait(self.locator.confirm_button)
        time.sleep(0.5)

    def search_origin_countries(self, country):
        self.click_and_wait(self.locator.search_input, clear=True, keys=country)
        self.click_and_wait(self.locator.search_button)


import os
import time
from constants.config import config
from pages.base_page import BasePage
from locators.locators import UnitsPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class UnitsPage(BasePage):

    def __init__(self, driver):
        self.url = os.path.join(config.BASE_URL, 'm-units')
        self.locator = UnitsPageLocators
        super().__init__(driver)

    def go_to_units_page(self):
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

    def select_checkbox_if_not_selected(self, locator):
        checkbox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        if not checkbox.is_selected():
            self.driver.execute_script("arguments[0].click();", checkbox)

    def new_unit(self, long_title, short_title, value_in_mm, desc):
        self.click_and_wait(self.locator.new_unit_button)
        self.click_and_wait(self.locator.long_title, clear=True, keys=long_title)
        self.click_and_wait(self.locator.short_title, clear=True, keys=short_title)
        self.click_and_wait(self.locator.value_in_mm, clear=True, keys=value_in_mm)
        self.select_checkbox_if_not_selected(self.locator.is_countable)
        self.select_checkbox_if_not_selected(self.locator.is_dimension)
        self.click_and_wait(self.locator.desc, keys=desc)
        self.click_and_wait(self.locator.save_button)
        time.sleep(1)

    def edit_unit(self, edit_long_title, edit_short_title, edit_value_in_mm, edit_desc):
        self.click_and_wait(self.locator.edit_button)
        self.click_and_wait(self.locator.long_title, clear=True, keys=edit_long_title)
        self.click_and_wait(self.locator.short_title, clear=True, keys=edit_short_title)
        self.click_and_wait(self.locator.value_in_mm, clear=True, keys=edit_value_in_mm)
        self.select_checkbox_if_not_selected(self.locator.is_countable)
        self.select_checkbox_if_not_selected(self.locator.is_dimension)
        self.click_and_wait(self.locator.desc, clear=True, keys=edit_desc)
        self.click_and_wait(self.locator.save_button)
        time.sleep(0.5)

    def delete_unit(self):
        self.click_and_wait(self.locator.delete_button)
        self.click_and_wait(self.locator.cancel_button)
        self.click_and_wait(self.locator.delete_button)
        self.click_and_wait(self.locator.confirm_button)
        time.sleep(0.5)

    def search_unit(self, long_title):
        self.click_and_wait(self.locator.search_input, clear=True, keys=long_title)
        self.click_and_wait(self.locator.search_button)

import os
import time
from constants.config import config
from pages.base_page import BasePage
from locators.locators import CategoriesPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class CategoriesPage(BasePage):

    def __init__(self, driver):
        self.url = os.path.join(config.BASE_URL, 'c-categories')
        self.locator = CategoriesPageLocators
        super().__init__(driver)

    def go_to_categories_page(self):
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

    def new_category(self, name, desc):
        self.click_and_wait(self.locator.new_category_button)
        self.click_and_wait(self.locator.parent_combobox)
        self.click_and_wait(self.locator.parent_option)
        self.click_and_wait(self.locator.name_input, keys=name)
        self.click_and_wait(self.locator.desc_input, keys=desc)
        self.click_and_wait(self.locator.save_button)

    def edit_category(self, name_edit, desc_edit):
        self.click_and_wait(self.locator.edit_button)
        self.click_and_wait(self.locator.parent_combobox)
        self.click_and_wait(self.locator.edit_parent_option)
        self.click_and_wait(self.locator.name_input, clear=True, keys=name_edit)
        self.click_and_wait(self.locator.desc_input, clear=True, keys=desc_edit)
        self.click_and_wait(self.locator.save_button)
    
    def delete_category(self):
        self.click_and_wait(self.locator.delete_button)
        self.click_and_wait(self.locator.cancel_button)
        self.click_and_wait(self.locator.delete_button)
        self.click_and_wait(self.locator.confirm_button)

    def search_category(self, name):
        self.click_and_wait(self.locator.search_input, clear=True, keys=name)
        self.click_and_wait(self.locator.search_button)
import os
import time
from constants.config import config
from pages.base_page import BasePage
from locators.locators import ProcessingsPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class ProcessingsPage(BasePage):

    def __init__(self, driver):
        self.url = os.path.join(config.BASE_URL, 'c-processings')
        self.locator = ProcessingsPageLocators
        super().__init__(driver)

    def go_to_processings_page(self):
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

    def new_processing(self, finishing_type, desc):
        self.click_and_wait(self.locator.new_processing_button)
        self.click_and_wait(self.locator.finishing_type_input, keys=finishing_type)
        self.select_checkbox_if_not_selected(self.locator.is_edge_processing)
        self.click_and_wait(self.locator.desc_input, keys=desc)
        self.click_and_wait(self.locator.save_button)

    def edit_processing(self, finishing_type_edit, desc_edit):
        self.click_and_wait(self.locator.edit_button)
        self.click_and_wait(self.locator.finishing_type_input, clear=True, keys=finishing_type_edit)
        self.click_and_wait(self.locator.desc_input, clear=True, keys=desc_edit)
        self.click_and_wait(self.locator.save_button)
    
    def delete_processing(self):
        self.click_and_wait(self.locator.delete_button)
        self.click_and_wait(self.locator.cancel_button)
        self.click_and_wait(self.locator.delete_button)
        self.click_and_wait(self.locator.confirm_button)

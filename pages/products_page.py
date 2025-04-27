import os
import time
from constants.config import config
from pages.base_page import BasePage
from locators.locators import ProductsPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class ProductsPage(BasePage):

    def __init__(self, driver):
        self.url = os.path.join(config.BASE_URL, 'c-products')
        self.locator = ProductsPageLocators
        super().__init__(driver)

    def go_to_products_page(self):
        self.go_to_page(self.url)

    def click_and_wait(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def send_keys_and_wait(self, locator, keys):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).send_keys(keys)

    def new_product(self, code, name, short_desc, length, height, width, thick, profit_rate, price_in_usd, cost_option, full_desc,
                    upload_image=None, upload_file=None):
        time.sleep(0.5)
        self.click_and_wait(ProductsPageLocators.new_product_button)
        self.click_and_wait(ProductsPageLocators.categories_combobox)
        self.click_and_wait(ProductsPageLocators.categories_option)
        self.click_and_wait(ProductsPageLocators.categories_multiselect_select)
        self.click_and_wait(ProductsPageLocators.type_combobox)
        self.click_and_wait(ProductsPageLocators.type_option)
        self.click_and_wait(ProductsPageLocators.origin_country_combobox)
        self.click_and_wait(ProductsPageLocators.origin_country_option)
        self.click_and_wait(ProductsPageLocators.processing_combobox)
        self.click_and_wait(ProductsPageLocators.processing_option)
        self.click_and_wait(ProductsPageLocators.parent_combobox)
        self.click_and_wait(ProductsPageLocators.parent_option)
        self.send_keys_and_wait(ProductsPageLocators.code_input, code)
        self.send_keys_and_wait(ProductsPageLocators.name_input, name)
        self.send_keys_and_wait(ProductsPageLocators.short_desc_input, short_desc)
        self.send_keys_and_wait(ProductsPageLocators.length_input, length)
        self.send_keys_and_wait(ProductsPageLocators.height_input, height)
        self.send_keys_and_wait(ProductsPageLocators.with_input, width)
        self.send_keys_and_wait(ProductsPageLocators.thick_input, thick)
        self.send_keys_and_wait(ProductsPageLocators.profit_rate_input, profit_rate)
        self.send_keys_and_wait(ProductsPageLocators.price_in_input, price_in_usd)
        self.click_and_wait(ProductsPageLocators.costs_combobox)
        self.click_and_wait(ProductsPageLocators.costs_option)
        self.click_and_wait(ProductsPageLocators.costs_multiselect_select)
        time.sleep(1)
        self.send_keys_and_wait(ProductsPageLocators.vat_option_input, cost_option)
        time.sleep(1)
        self.send_keys_and_wait(ProductsPageLocators.full_desc_input, full_desc)

        if upload_image and os.path.exists(upload_image):
            file_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.locator.image_input))
            file_input.send_keys(upload_image)
        else:
            raise FileNotFoundError(f"Image does not exist: {upload_image}")

        if upload_file and os.path.exists(upload_file):
            file_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.locator.file_input))
            file_input.send_keys(upload_file)
        else:
            raise FileNotFoundError(f"File does not exist: {upload_file}")

        time.sleep(3)
        self.click_and_wait(ProductsPageLocators.save_button)

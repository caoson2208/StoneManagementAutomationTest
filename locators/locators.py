import os
from selenium.webdriver.common.by import By
from constants.config import config


class BasePageLocators:
    save_button = (By.CSS_SELECTOR, "button[type='submit']")
    edit_button = (By.XPATH, "(//a[@title='Edit'])[last()]")
    delete_button = (By.XPATH, "(//button[@title='Delete'])[last()]")
    confirm_button = (By.XPATH, "//button[contains(@class, 'vue-dialog-button')]//span[contains(@class, 'btn-danger')]")
    cancel_button = (By.XPATH, "//button[contains(text(), 'No, cancel.')]")
    search_input = (By.CSS_SELECTOR, "input.form-control[placeholder='Search']")
    search_button = (By.CSS_SELECTOR, "button.btn.btn-primary[type='button']")

class LoginPageLocators(BasePageLocators):
    username_input = (By.ID, "email")
    password_input = (By.ID, "password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    profile = (By.CSS_SELECTOR, "a.dropdown-toggle.nav-link")
    logout_link = (By.XPATH, f"//a[@href='{config.HOME_URL}/logout']")

class CountriesPageLocators(BasePageLocators):
    new_country_button = (By.XPATH, f"//a[@href='{config.HOME_URL}/m-countries/create' and contains(@class, 'btn-primary')]")
    name_input = (By.ID, "name")
    code_input = (By.ID, "code")
    desc_input = (By.ID, "description")

class UnitsPageLocators(BasePageLocators):
    new_unit_button = (By.XPATH, f"//a[@href='{config.HOME_URL}/m-units/create' and contains(@class, 'btn-primary')]")
    long_title = (By.ID, "long_title")
    short_title = (By.ID, "short_title")
    value_in_mm = (By.ID, "value_in_mm")
    is_countable = (By.XPATH, "//label[contains(.,'Is countable')]")
    is_dimension = (By.ID, "is_dimension")
    desc = (By.ID, "description")

class OriginCountriesPageLocators(BasePageLocators):
    new_origin_country_button = (By.XPATH, f"//a[@href='{config.HOME_URL}/c-origin-countries/create' and contains(@class, 'btn-primary')]")
    origin_country_combobox = (By.XPATH, "//div[@role='combobox' and @aria-owns='listbox-m_country_id']")
    origin_country_id = 2
    origin_country_option = (By.XPATH, f"//li[@id='m_country_id-{origin_country_id}']")
    edit_origin_country_id = 3
    edit_origin_country_option = (By.XPATH, f"//li[@id='m_country_id-{edit_origin_country_id}']")

class CategoriesPageLocators(BasePageLocators):
    new_category_button = (By.XPATH, f"//a[@href='{config.HOME_URL}/c-categories/create' and contains(@class, 'btn-primary')]")
    parent_combobox = (By.XPATH, "//div[@role='combobox' and @aria-owns='listbox-parent_id']")
    parent_id = 2
    parent_option = (By.XPATH, f"//li[@id='parent_id-{parent_id}']")
    name_input = (By.ID, "name")
    desc_input = (By.ID, "description")
    edit_parent_id = 3
    edit_parent_option = (By.XPATH, f"//li[@id='parent_id-{parent_id}']")

class  ProcessingsPageLocators(BasePageLocators):
    new_processing_button = (By.XPATH, f"//a[@href='{config.HOME_URL}/c-processings/create' and contains(@class, 'btn-primary')]")
    finishing_type_input = (By.ID, "finishing_type")
    is_edge_processing = (By.XPATH, "//label[contains(.,'Is edge processing')]")
    desc_input = (By.XPATH, "description")

class  TypesPageLocators(BasePageLocators):
    new_type_button = (By.XPATH, f"//a[@href='{config.HOME_URL}/c-types/create' and contains(@class, 'btn-primary')]")
    type_input = (By.ID, "type")
    desc_input = (By.ID, "description")


class ProductsPageLocators(BasePageLocators):
    new_product_button = (By.XPATH, f"//a[@href='{config.HOME_URL}/c-products/create' and contains(@class, 'btn-primary')]")
    categories_combobox = (By.XPATH, "//div[@role='combobox' and @aria-owns='listbox-categories']")
    categories_option_select = "Đá Onyx"
    categories_option = (By.XPATH, f"//li[@role='option' and contains(., '{categories_option_select}')]")
    categories_multiselect_select = (By.CSS_SELECTOR, "div[role='combobox'][aria-owns='listbox-categories'] div.multiselect__select")
    type_combobox = (By.XPATH, "//div[@role='combobox' and @aria-owns='listbox-c_type_id']")
    type_option_id = 1
    type_option = (By.XPATH, f"//li[@id='c_type_id-{type_option_id}']")
    origin_country_combobox = (By.XPATH, "//div[@role='combobox' and @aria-owns='listbox-c_origin_country_id']")
    origin_country_id = 2
    origin_country_option = (By.XPATH, f"//li[@id='c_origin_country_id-{origin_country_id}']")
    processing_combobox = (By.XPATH, "//div[@role='combobox' and @aria-owns='listbox-c_processing_id']")
    processing_id = 1
    processing_option = (By.XPATH, f"//li[@id='c_processing_id-{processing_id}']")
    parent_combobox = (By.XPATH, "//div[@role='combobox' and @aria-owns='listbox-parent_id']")
    parent_id = 2
    parent_option = (By.XPATH, f"//li[@id='parent_id-{parent_id}']")
    code_input = (By.ID, "code")
    name_input = (By.ID, "name")
    short_desc_input = (By.ID, "short_description")
    length_input = (By.ID, "length_in_mm")
    height_input = (By.ID, "height_in_mm")
    with_input = (By.ID, "width_in_mm")
    thick_input = (By.ID, "thick_in_mm")
    profit_rate_input = (By.ID, "profit_rate")
    price_in_input = (By.ID, "price_in_usd")
    is_active_checkbox = (By.NAME, "is_active_fake_element")
    use_thick_checkbox = (By.NAME, "use_thick_fake_element")
    costs_combobox = (By.XPATH, "//div[@role='combobox' and @aria-owns='listbox-null']")
    costs_id = 3
    costs_option = (By.XPATH, f"//li[@id='null-{costs_id}']")
    costs_multiselect_select = (By.CSS_SELECTOR, "div[role='combobox'][aria-owns='listbox-null'] div.multiselect__select")
    vat_option_input = (By.NAME, "c_sales_costs.vat.cost_in_usd")
    full_desc_input = (By.CLASS_NAME, "trumbowyg-editor")
    image_input = (By.XPATH, "//input[@type='file' and @accept='image/*, video/*']")
    file_input = (By.XPATH, "//input[@type='file' and @accept='application/pdf, application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document, application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']")

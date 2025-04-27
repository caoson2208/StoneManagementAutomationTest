import time
import pytest
from pages.countries_page import CountriesPage
from tests.base_test import BaseTest
from constants.config import config


class TestCountries(BaseTest):
    @pytest.fixture
    def load_pages(self):
        self.page = CountriesPage(self.driver)
        self.page.go_to_countries_page()
        self.load_cookies()
        self.page.go_to_countries_page()

    def test_successful_countries(self, load_pages: None):
        self.page.new_country('test name', 'code', 'test desc')
        self.page.search_country('test name')
        self.page.edit_country('edit name', 'co', 'edit desc')
        self.page.delete_country()
        time.sleep(3)

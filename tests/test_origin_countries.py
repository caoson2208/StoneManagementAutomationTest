import time
import pytest
from pages.origin_countries_page import OriginCountriesPage
from tests.base_test import BaseTest
from constants.config import config


class TestCountries(BaseTest):
    @pytest.fixture
    def load_pages(self):
        self.page = OriginCountriesPage(self.driver)
        self.page.go_to_origin_countries_page()
        self.load_cookies()
        self.page.go_to_origin_countries_page()

    def test_successful_origin_countries(self, load_pages: None):
        self.page.new_origin_countries()
        self.page.search_origin_countries("Finland")
        self.page.edit_origin_countries()
        self.page.delete_origin_countries()
        time.sleep(1)

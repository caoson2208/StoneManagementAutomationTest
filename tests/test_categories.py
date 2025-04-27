import time
import pytest
from pages.categories_page import CategoriesPage
from tests.base_test import BaseTest
from constants.config import config


class TestCategories(BaseTest):
    @pytest.fixture
    def load_pages(self):
        self.page = CategoriesPage(self.driver)
        self.page.go_to_categories_page()
        self.load_cookies()
        self.page.go_to_categories_page()

    def test_successful_category(self, load_pages: None):
        self.page.new_category("test name", "test desc")
        self.page.search_category("test name")
        self.page.edit_category("edit name", "edit desc")
        self.page.delete_category()
        time.sleep(1)

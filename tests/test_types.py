import time
import pytest
from pages.types_page import TypesPage
from tests.base_test import BaseTest
from constants.config import config


class TestUnits(BaseTest):
    @pytest.fixture
    def load_pages(self):
        self.page = TypesPage(self.driver)
        self.page.go_to_types_page()
        self.load_cookies()
        self.page.go_to_types_page()

    def test_successful_types(self, load_pages: None):
        self.page.new_type('test type','test description')
        self.page.edit_type('edit type', 'edit description')
        self.page.delete_type()
        time.sleep(3)

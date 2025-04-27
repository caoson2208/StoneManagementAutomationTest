import time
import pytest
from pages.units_page import UnitsPage
from tests.base_test import BaseTest
from constants.config import config


class TestUnits(BaseTest):
    @pytest.fixture
    def load_pages(self):
        self.page = UnitsPage(self.driver)
        self.page.go_to_units_page()
        self.load_cookies()
        self.page.go_to_units_page()

    def test_successful_units(self, load_pages: None):
        self.page.new_unit('test long title', 'test short title', 15.5, 'test description')
        self.page.search_unit('test long title')
        self.page.edit_unit('edit long title', 'edit short title', 10.5, 'edit description')
        self.page.delete_unit()
        time.sleep(3)

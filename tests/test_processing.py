import time
import pytest
from pages.processings_page import ProcessingsPage
from tests.base_test import BaseTest
from constants.config import config


class TestUnits(BaseTest):
    @pytest.fixture
    def load_pages(self):
        self.page = ProcessingsPage(self.driver)
        self.page.go_to_processings_page()
        self.load_cookies()
        self.page.go_to_processings_page()

    def test_successful_processings(self, load_pages: None):
        self.page.new_processing('test finishing type', 'test description')
        self.page.edit_processing('edit finishing type', 'edit description')
        self.page.delete_processing()
        time.sleep(3)

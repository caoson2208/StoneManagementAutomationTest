import time
import os
import pytest
from pages.products_page import ProductsPage
from tests.base_test import BaseTest
from constants.config import config


class TestCountries(BaseTest):
    @pytest.fixture
    def load_pages(self):
        self.page = ProductsPage(self.driver)
        self.page.go_to_products_page()
        self.load_cookies()
        self.page.go_to_products_page()

    def test_successful_product(self, load_pages: None):
        upload_image = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "test_stone.png"))
        if os.path.exists(upload_image):
            print(f"File exists: {upload_image}")
        else:
            print(f"File does not exist: {upload_image}")

        upload_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "test_pdf.pdf"))
        if os.path.exists(upload_file):
            print(f"File exists: {upload_file}")
        else:
            print(f"File does not exist: {upload_file}")

        self.page.new_product(
            "new code", "new name", "new short desc", 2000, 3000,
            1500, 17, 40, 15000, 10, "new full desc", upload_image,
            upload_file
        )
        time.sleep(5)

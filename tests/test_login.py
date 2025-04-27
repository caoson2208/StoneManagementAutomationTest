import pytest
import pickle
import os
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from constants.config import config


class TestLogin(BaseTest):

    @pytest.fixture
    def load_pages(self):
        self.page = LoginPage(self.driver)
        self.page.go_to_login_page()

    def test_successful_login(self, load_pages: None):
        self.page.set_user_inputs("admin@dms.com", "7349yiey@939FF")
        assert self.driver.current_url == config.HOME_URL, f"URL không đúng, hiện tại là: {self.driver.current_url}"
        cookies = self.driver.get_cookies()
        # Create path to folder data
        data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
        # Make sure the data directory exists
        os.makedirs(data_dir, exist_ok=True)
        # Create the full path for the cookie file
        cookie_path = os.path.join(data_dir, 'cookies.pkl')
        # Save cookie
        with open(cookie_path, "wb") as f:
            pickle.dump(cookies, f)


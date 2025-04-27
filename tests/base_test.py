import os
import pickle
import warnings
import pytest
import yaml
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.edge.service import Service as ServiceEdge
from selenium.webdriver.firefox.service import Service as ServiceFirefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

os.environ['WDM_LOG_LEVEL'] = '0'


def load_config():
    path = Path(__file__).parent / "../config.yaml"
    with open(path) as config_file:
        return yaml.safe_load(config_file)


# Tải config một lần khi module được import
CONFIG = load_config()


class BaseTest:

    @pytest.fixture(autouse=True)
    def init_driver(self):
        warnings.simplefilter("ignore", ResourceWarning)
        if CONFIG['browser'] == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--start-maximized')
            if CONFIG['headless']:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
            self.driver = webdriver.Chrome(service=ServiceChrome(ChromeDriverManager().install()), options=options)
        elif CONFIG['browser'] == 'firefox':
            options = webdriver.FirefoxOptions()
            options.add_argument('--start-maximized')
            if CONFIG['headless']:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
            self.driver = webdriver.Firefox(service=ServiceFirefox(GeckoDriverManager().install()), options=options)
            if not CONFIG['headless']:
                self.driver.maximize_window()
        elif CONFIG['browser'] == 'edge':
            options = webdriver.EdgeOptions()
            options.add_argument('--start-maximized')
            if CONFIG['headless']:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
            self.driver = webdriver.Edge(service=ServiceEdge(EdgeChromiumDriverManager().install()), options=options)
            if not CONFIG['headless']:
                self.driver.maximize_window()
        else:
            raise Exception("Incorrect Browser")

        self.wait = WebDriverWait(self.driver, CONFIG.get('timeout', 10))
        yield self.wait, self.driver

        if self.driver is not None:
            self.driver.quit()

    def load_cookies(self):
        data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
        cookie_file = os.path.join(data_dir, 'cookies.pkl')
        if os.path.exists(cookie_file):
            with open(cookie_file, "rb") as f:
                cookies = pickle.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()  # Refresh để áp dụng cookie
            return True
        return False


# Các biến config có thể được truy cập trực tiếp nếu cần
BROWSER = CONFIG['browser']
HEADLESS = CONFIG['headless']
TIMEOUT = CONFIG.get('timeout', 10)

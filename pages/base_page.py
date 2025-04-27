class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

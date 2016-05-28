from pscore.config.test_configuration import TestConfiguration as Config


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def config(self):
        return Config

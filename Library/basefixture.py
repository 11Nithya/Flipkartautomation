from selenium import webdriver
from Library.config import Config
import pytest
from time import sleep

class Driverinit:

    @pytest.fixture(scope="class", autouse=True)
    def driver_init(self, request):
        driver= webdriver.Chrome(Config.chromepath)
        request.cls.driver = driver
        driver.get(Config.url)


        driver.maximize_window()
        # driver.implicitly_wait(30)
        # sleep(10)
        yield
        print(driver.title)
        driver.quit()


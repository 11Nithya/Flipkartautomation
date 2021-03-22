from selenium import webdriver
from config import *
import pytest


class Driverinit:

    @pytest.fixture(scope="class", autouse=True)
    def driver_init(self, request):
        if browser.lower()=="chrome":
            driver= webdriver.Chrome(chromepath)

        elif browser.lower()=="firefox":
            driver= webdriver.firefox()


        request.cls.driver= driver

        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(30)
        yield
        print(driver.title)
        driver.quit()
from Library.config import Config
from Library.webutli import Generic_method
from Library.file import ReadJson
import time

read_json = ReadJson()
obj1 = Generic_method()
element = read_json.read_locators(Config.OBJ_JSON)

class Cart:
    def __init__(self, driver):
        self.driver = driver

    def click_on_place_order(self):
        "clicks on place order"
        obj1.wait_and_click(self.driver, element["clickOnPlaceOrder"])

    def click_on_remove(self):
        "clicks on remove"
        obj1.wait_and_click(self.driver, element["clickonremove"])

    def click_remove(self):
        "clicks on remove pop up"
        obj1.wait_and_click(self.driver, element['remove'])



from Library.config import Config
from Library.webutli import Generic_method
from Library.file import ReadJson
import time

read_json = ReadJson()
obj1 = Generic_method()
element = read_json.read_locators(Config.OBJ_JSON)


class Product_details:

    def __init__(self, driver):
        self.driver = driver


    def click_on_cart(self):
        "clicks on add to cart"
        obj1.wait_and_click(self.driver, element["clickon_cart"])

    def click_on_buy(self):
        "clicks on buy"
        obj1.wait_and_click(self.driver, element['clickon_buy'])
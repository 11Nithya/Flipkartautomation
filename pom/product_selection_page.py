from Library.config import Config
from Library.webutli import Generic_method
from Library.file import ReadJson
import time

read_json = ReadJson()
obj1 = Generic_method()
element = read_json.read_locators(Config.OBJ_JSON)


class Productpage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_fassured(self):
        "clicks on flipkart assured check box"
        obj1.wait_and_click(self.driver, element['clickOnfAssured'])

    def click_on_gran(self):
        "click on the game"
        obj1.wait_and_click(self.driver, element["clickon_gran"])

    def switch_tab(self):
        "switches the window"
        obj1.switch_to(self.driver)



    def click_on_buy(self):
        "clicks on buy"
        obj1.wait_and_click(self.driver, element['clickon_buy'])

    def click_on_mi(self):
        "clicks on mi"
        obj1.wait_and_click(self.driver, element['clickon_Mi'])


    def click_on_price(self):
        "clicks on price"
        obj1.select_class(self.driver,element["clickon_price"])

    def click_on_fastrack(self):
        "clicks on fastrack brand"
        obj1.click_on(self.driver,element['clickon_fastrack'])

    def click_on_watch(self):
        "click on watch"
        obj1.wait_and_click(self.driver,element['clickon_watch'])


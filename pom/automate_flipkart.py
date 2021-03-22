from config import *
from Library.file import Reader
from Library.webutli import Generic_method
import time


obj= Reader()
element, keys= obj.wbreader(obj_filename, obj_sheetname)
obj1= Generic_method()

class Flipkart:

    def __init__(self,driver):
        self.driver = driver
        # self.file_testcase= file_testcase
        # self.item = obj.wbvalue(test_data_filename,test_data_sheetname,self.file_testcase)


    def handle_popup(self):
        obj1.click_on(self.driver, element["close_popup"])

    def search_on_item(self):
        obj1.search_item(self.driver,element["click_search"], "playstation 5 games")

    def click_on_magnify(self):
        obj1.click_magnify(self.driver, element["clickon_magnify"])

    def click_on_gran(self):
        obj1.click_on(self.driver, element["clickOnGTA"])

    def switch_tab(self):
        obj1.switch_to(self.driver)

    def click_on_cart(self):
        obj1.click_on(self.driver, element["clickon_cart"])

    # def click_cart(self):
    #     obj1.click_on(self.driver, element["clickcart"])

    def click_on_place_order(self):
        obj1.click_on(self.driver, element["clickOnPlaceOrder"])

    def click_on_fassured(self):
        obj1.click_on(self.driver, element['clickOnfAssured'])

    def close_the_tab(self):
        obj1.close_tab(self.driver)
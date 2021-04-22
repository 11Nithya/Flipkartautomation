from Library.config import Config
from Library.webutli import Generic_method
from Library.file import ReadJson
import time

read_json = ReadJson()
obj1 = Generic_method()
element = read_json.read_locators(Config.OBJ_JSON)


class Flipkart:

    def __init__(self, driver):
        self.driver = driver
        # self.series= series
        # self.game= game

    def handle_popup(self):
        "clicks on popup"
        obj1.click_on(self.driver, element["close_popup"])

    def search_on_item(self):
        "clicks on playstation 5 games"
        obj1.search_item(self.driver,element["click_search"], "playstation 5 games")

    def click_on_magnify(self):
        "clicks on search icon"
        obj1.click_magnify(self.driver, element["clickon_magnify"])


    def search_on_item2(self):
        "searches for watches"
        obj1.search_item(self.driver,element["click_search"], "watches")


    def click_on_view(self):
        "clicks on view all"
        obj1.wait_and_click(self.driver,element['clickon_view'])

    def click_on_products(self):
        "click on products "
        obj1.products(self.driver,element['clickon_products'])


    def click_on_menus(self):
        "click on specified menu"
        obj1.products(self.driver,element['clickon_menus'])

    def mouse_hover(self):
        "performs mouse hover action on specified element"
        obj1.hover_all(self.driver,element['clickon_home'])


    def grab_menu(self):
        "grabs all the menu"
        obj1.grab(self.driver,element['graball_menu'])


    def click_on_electronics(self):
        "movuse hover on electronics"
        obj1.hover_all(self.driver,element['clickon_Electonics'])

    def click_on_Computer(self):
        "mouse hover on computer"
        obj1.hover_all(self.driver,element['clickon_Computer'])

    def click_on_all(self):
        "clicks on all"
        obj1.wait_and_click(self.driver,element['clickon_All'])

    def click_on_mi(self):
        "clicks on mi"
        obj1.wait_and_click(self.driver,element['clickon_Mi'])





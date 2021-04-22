"Search for watch which is of fastrack and price is above 2000 and buy the product"


import pytest
from Library.config import Config
from pom.Home_page import Flipkart
from Library.basefixture import Driverinit
from Library.file import ReadJson
from pom.product_selection_page import Productpage
from pom.particular_product_details import Product_details
from pom.Cart import Cart
import time

read_json= ReadJson()

class Test_Flipkart(Driverinit):

    def test_buying_a_product(self):
        "search for fastrack watch within 3000 and clicks on buy"

        flip= Flipkart(self.driver)
        selection=Productpage(self.driver)
        details= Product_details(self.driver)
        cart = Cart(self.driver)
        flip.handle_popup()
        flip.search_on_item2()
        flip.click_on_magnify()
        selection.click_on_price()
        time.sleep(2)
        selection.click_on_fastrack()
        selection.click_on_watch()
        selection.switch_tab()
        time.sleep(3)
        details.click_on_buy()

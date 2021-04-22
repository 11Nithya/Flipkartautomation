"Search for playstation 5 games clicks on any one of the game and add to cartand places the order"

import pytest
from Library.config import Config
import json
from pom.Home_page import Flipkart
from pom.product_selection_page import Productpage
from pom.particular_product_details import Product_details
from pom.Cart import Cart
from Library.basefixture import Driverinit
from Library.file import ReadJson
import time

read_json= ReadJson()


#test_data=read_json.read_test_data(Config.TEST_JSON)

#@pytest.mark.parametrize("series , game", test_data)
class Test_Flipkart(Driverinit):


    def test_placing_the_order(self):
        "search for playstation 5 games clicks on any one of the game and add to cart and places the order"
        flip= Flipkart(self.driver)
        selection= Productpage(self.driver)
        details=Product_details(self.driver)
        cart= Cart(self.driver)
        flip.handle_popup()
        flip.search_on_item()
        flip.click_on_magnify()
        selection.click_on_fassured()
        selection.click_on_gran()
        selection.switch_tab()
        details.click_on_cart()
        cart.click_on_place_order()



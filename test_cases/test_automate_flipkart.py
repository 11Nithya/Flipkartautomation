"Search for playstation 5 games clicks on any one of the game and add to cartand places the order"

import pytest
from Library.config import Config
import json
from pom.automate_flipkart import Flipkart
from Library.basefixture import Driverinit
from Library.file import ReadJson
import time

read_json= ReadJson()

#test_data=read_json.read_test_data(Config.TEST_JSON)

#@pytest.mark.parametrize("series , game", test_data)
class Test_Flipkart(Driverinit):


    def test_obj(self):
        "search for playstation 5 games clicks on any one of the game and add to cartand places the order"
        flip= Flipkart(self.driver)
        flip.handle_popup()
        flip.search_on_item()
        flip.click_on_magnify()
        flip.click_on_fassured()
        time.sleep(3)
        flip.click_on_gran()
        flip.switch_tab()
        flip.click_on_cart()
        flip.click_on_place_order()


        # flip.click_on_remove()
        # time.sleep(3)
        # flip.click_on_alert()

        # flip.click_on_place_order()
        # time.sleep(4)
        # flip.close_the_tab()
        # time.sleep(3)



        # flip.search_items2()

        # flip.switch_tab3()
        # time.sleep(3)
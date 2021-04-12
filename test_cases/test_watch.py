"Search for watch which is of fastrack and price is above 2000 and buy the product"


import pytest
from Library.config import Config
from pom.automate_flipkart import Flipkart
from Library.basefixture import Driverinit
from Library.file import ReadJson
import time

read_json= ReadJson()

class Test_Flipkart(Driverinit):

    def test_obj(self):
        "search fpr fastrack watch above 2000 and clicks on buy"

        flip= Flipkart(self.driver)
        flip.handle_popup()
        flip.search_on_item2()
        flip.click_on_magnify()
        flip.click_on_price()
        time.sleep(2)
        flip.click_on_fastrack()

        flip.click_on_watch()
        flip.switch_tab()

        flip.click_on_buy()

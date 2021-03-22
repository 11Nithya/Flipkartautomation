import pytest

from pom.automate_flipkart import Flipkart
from Library.basefixture import Driverinit
import time
# from Library.file import Reader
# from config import *

class Test_Flipkart(Driverinit):


    def test_obj(self):

        flip= Flipkart(self.driver)
        flip.handle_popup()
        time.sleep(2)
        flip.search_on_item()
        time.sleep(2)
        flip.click_on_magnify()
        time.sleep(2)
        flip.click_on_fassured()
        time.sleep(2)
        flip.click_on_gran()
        time.sleep(2)
        flip.switch_tab()
        time.sleep(3)
        flip.click_on_cart()
        time.sleep(2)
        flip.click_on_place_order()
        time.sleep(2)
        flip.close_the_tab()
        time.sleep(3)
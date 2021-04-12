"mouse hovers on electronics and computer clicks on all clicks on mi adds to the card and removes it"

from pom.automate_flipkart import Flipkart
from Library.basefixture import Driverinit
from Library.file import ReadJson
import time

read_json= ReadJson()

class Test_Flipkart(Driverinit):

    def test_obj(self):
        "mouse hovers on electronics and computer clicks on all clicks on mi adds to the card and removes it"

        flip= Flipkart(self.driver)
        flip.handle_popup()
        flip.click_on_electronics()
        flip.click_on_Computer()
        flip.click_on_all()
        time.sleep(3)
        flip.click_on_mi()
        flip.switch_tab()
        flip.click_on_cart()
        time.sleep(3)
        flip.click_on_remove()
        flip.click_remove()
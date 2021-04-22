"mouse hovers on electronics and computer clicks on all clicks on mi adds to the card and removes it"

from pom.Home_page import Flipkart
from pom.product_selection_page import Productpage
from pom.particular_product_details import Product_details
from pom.Cart import Cart
from Library.basefixture import Driverinit
from Library.file import ReadJson
import time

read_json= ReadJson()

class Test_Flipkart(Driverinit):

    def test_remove_the_item_from_cart(self):
        "mouse hovers on electronics and computer clicks on all clicks on mi adds to the card and removes it"

        flip= Flipkart(self.driver)
        selection = Productpage(self.driver)
        details = Product_details(self.driver)
        cart = Cart(self.driver)
        flip.handle_popup()
        flip.click_on_electronics()
        flip.click_on_Computer()
        flip.click_on_all()
        time.sleep(3)
        selection.click_on_mi()
        selection.switch_tab()
        details.click_on_cart()
        time.sleep(3)
        cart.click_on_remove()
        cart.click_remove()
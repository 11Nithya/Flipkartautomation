"Displays deal of the day products"


from pom.Home_page import Flipkart
from Library.basefixture import Driverinit
from Library.file import ReadJson
import time

read_json= ReadJson()

class Test_Flipkart(Driverinit):

    def test_deal_of_the_day(self):
        "displays all the deals of the products"

        flip= Flipkart(self.driver)
        flip.handle_popup()
        flip.click_on_view()
        time.sleep(2)
        flip.click_on_products()
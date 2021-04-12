"move hover on all menu and displays all the menus"


from pom.automate_flipkart import Flipkart
from Library.basefixture import Driverinit
from Library.file import ReadJson
import time

read_json= ReadJson()

class Test_Flipkart(Driverinit):

    def test_obj(self):
        """move hover on all menu and displays all the menus """

        flip= Flipkart(self.driver)
        flip.handle_popup()
        flip.grab_menu()

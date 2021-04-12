"move hover home menu and displays all the submenus in home"


from pom.automate_flipkart import Flipkart
from Library.basefixture import Driverinit
from Library.file import ReadJson
import time

read_json= ReadJson()

class Test_Flipkart(Driverinit):

    def test_obj(self):
        """move hover home menu and displays all the submenus in home"""

        flip= Flipkart(self.driver)
        flip.handle_popup()
        flip.mouse_hover()
        flip.click_on_menus()

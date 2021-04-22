"move hover home menu and displays all the submenus in home"


from pom.Home_page import Flipkart
from Library.basefixture import Driverinit
from Library.file import ReadJson
import time

read_json= ReadJson()

class Test_Flipkart(Driverinit):

    def test_display_the_submenu_of_home(self):
        """move hover home menu and displays all the submenus in home"""

        flip= Flipkart(self.driver)
        flip.handle_popup()
        flip.mouse_hover()
        flip.click_on_menus()

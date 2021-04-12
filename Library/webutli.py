from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Generic_method:

    def click_on(self,driver,element):
        "clicks on element"
        loctype, locvalue = element
        driver.find_element(loctype,locvalue).click()

    def wait_and_click(self, driver, element):
        "clicks on specified element with wait condition"
        By.Xpath, locvalue = element
        wait = WebDriverWait(driver,30)
        wait.until(ec.visibility_of_element_located((By.Xpath,locvalue)))  #wait.until(ec.visibility_of_element_located((loctype,locvalue)))
        driver.find_element(By.Xpath,locvalue).click()

    def select_class(self,driver,element):
        "select the checkbox"
        wait = WebDriverWait(driver, 30)
        By.XPATH, locvalue = element
        select = Select(wait.until(ec.visibility_of_element_located((By.XPATH, locvalue))))
        select.select_by_value("3000")


    def search_item(self,driver,element,string):
        "search for the item"
        loctype, locvalue = element
        driver.find_element(loctype,locvalue).send_keys(str(string))

    def click_magnify(self,driver, element):
        "clicks on search icon"
        loctype, locvalue = element
        driver.find_element(loctype,locvalue).click()


    def switch_to(self,driver):
        "swifts from one window to another"
        handles=driver.window_handles
        driver.switch_to.window(handles[1])

    def add_to_cart(self,driver,element):
        "clicks on add cart button"
        loctype, locvalue = element
        driver.find_element(loctype, locvalue).click()


    def click_to_cart(self,driver,element):
        "clicks on element"
        loctype, locvalue = element
        driver.find_element(loctype, locvalue).click()



    def switch_back(self,driver):
        "switches back to parent window"
        handles=driver.window_handles
        driver.switch_to.window(handles[0])

    def grab(self,driver,element):
        "grabs the menu"
        loctype,locvalue=element
        menus=driver.find_elements(loctype,locvalue)
        for menu in menus:
            print(menu.text)



    def hover_all(self,driver,element):
        "mouse hovers on specified element"
        loctype,locvalue=element
        elem=driver.find_element(loctype,locvalue)
        actions= ActionChains(driver)
        actions.move_to_element(elem).perform()




    def products(self,driver,element):
        """loops over all the products and displays products names"""
        loctype,locvalue=element
        product = driver.find_elements(loctype,locvalue)
        for item in product:
            print(item.text)



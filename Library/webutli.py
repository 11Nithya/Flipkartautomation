

class Generic_method:

    def click_on(self,driver,element):
        loctype, locvalue = element
        driver.find_element(loctype,locvalue).click()

    def search_item(self,driver,element,string):
        loctype,locvalue= element
        driver.find_element(loctype,locvalue).send_keys(str(string))

    def click_magnify(self,driver, element):
        loctype, locvalue= element
        driver.find_element(loctype,locvalue).click()


    def switch_to(self,driver):
        handles=driver.window_handles
        driver.switch_to.window(handles[1])

    def add_to_cart(self,driver,element):
        loctype, locvalue= element
        driver.find_element(loctype, locvalue).click()

    def click_to_cart(self,driver,element):
        loctype, locvalue = element
        driver.find_element(loctype,loctype).click()

    def close_tab(self, driver):
        driver.close()



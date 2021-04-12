from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Library.config import Config
# from expected_values import DROP_DOWNNS
driver= webdriver.Chrome(Config.chromepath)
driver.get(Config.url)
driver.find_element_by_xpath('//button[@class="_2KpZ6l _2doB4z"]').click()
menus=driver.find_elements_by_xpath('//div[@class="xtXmba"]')
menus=[menu.text for menu in menus]
print(menus)
 actions= ActionChains(driver)
for menu in menus:
    print(menu.upper())
    actions.move_to_element(driver.find_element_by_xpath(f"//div[text()='{menu}']")).perform()
    submenus= driver.find_elements_by_xpath("//a[contains(@class,'_6WOcW9')]")
    submenus=[menu.text for menu in submenus]
    print(submenus)
    print()

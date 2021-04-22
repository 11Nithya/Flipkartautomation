
import json
from Library.config import Config

data={

    'close_popup':{'loctype': 'xpath',
                   'locvalue':'//button[@class="_2KpZ6l _2doB4z"]'},

    'click_search': {'loctype':'xpath',
                     'locvalue': "//div/input[@type='text' and @name='q']"},

    'clickon_magnify':{'loctype': 'xpath',
                        'locvalue': '//button[@class="L0Z3Pu"]'},

    'clickon_gran' : {'loctype': 'xpath',
                      'locvalue': '//a[text()="Kebilshop 5V PSP Charger/ Adapter For PSP 1000/2000/300..."]'},

    'clickon_cart' : {'loctype': 'xpath',
                      'locvalue': "//button[@class='_2KpZ6l _2U9uOA _3v1-ww']"},

    'clickOnPlaceOrder' : {'loctype': 'xpath',
                           'locvalue': "//button//span[text()='Place Order']"},

    'clickOnfAssured' : {'loctype': 'xpath',
                         'locvalue': "//label/div[@class='_24_Dny _3tCU7L']"},

    'clickon_Electonics':{'loctype':'xpath',
                           'locvalue':'//div[text()="Electronics"]'},

    'clickon_Computer':{'loctype':'xpath',
                         'locvalue':'//a[text()="Computer Peripherals"]'},

    'clickon_All': {'loctype': 'xpath',
                         'locvalue': '//a[text()="All"]'},

    'clickon_Mi' : {'loctype': 'xpath',
                     'locvalue':'//a[text()="Mi TV Stick with Built in Chromecast"]'},


    'clickonremove' : { 'loctype': 'xpath',
                        'locvalue': '(//div[@class="_3dsJAO"])[2]'},

    'remove': {'loctype': 'xpath',
                'locvalue': '//div//div[@class="_3dsJAO _24d-qY FhkMJZ"]'},

    'clickon_price': {'loctype':'xpath',
                      'locvalue':"(//div//select)[2]"},


    'clickon_fastrack':{'loctype':'xpath',
                        'locvalue':"//div[@class='_24_Dny']"},

    'clickon_watch':{'loctype':'xpath',
                     'locvalue' :'//a[text()="9915PP56 Minimalists Analog Watch  - For Men & Women"]'},

    'clickon_buy':{'loctype':'xpath',
                   'locvalue':'//form//button[@class="_2KpZ6l _2U9uOA ihZ75k _3AWRsL"]'},

    'graball_menu':{'loctype':'xpath',
                     'locvalue':'//div[@class="xtXmba"]'},


    'clickon_view':{'loctype': 'xpath',
                    'locvalue':'//a[@class="_2KpZ6l _3dESVI"]'},

    'clickon_products':{'loctype':'xpath',
                        'locvalue':'//a//div[@class="_3LU4EM"]'},

    'clickon_home':{'loctype':'xpath',
                   'locvalue':'//div[text()="Home"]'},

    'clickon_menus':{'loctype':'xpath',
                     'locvalue':'//a//div[@class="_3XS_gI _7qr1OC"]'}





}

fileobj= open(Config.OBJ_JSON,"w+")
json.dump(data, fileobj, indent=4)

fileobj=open(Config.OBJ_JSON,"r")
json.load(fileobj)

fileobj.close()

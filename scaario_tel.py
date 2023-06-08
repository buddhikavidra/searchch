from pages.locators import PageLocators
from pages.tel_directory import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import os
from webdriver_manager.chrome import ChromeDriverManager
import configparser


current_directory = os.getcwd()
config = configparser.ConfigParser()
config.read('config.ini')
profile = config.get('DEFAULT','profile')
link = config.get('DEFAULT','link')



def test_email_login_with_correct_code(browser):
    page = LoginPage(browser, link)
    page.open()
    page.who_what_field("bar")
    page.where_field("France")
    page.click_submit()
    page.pause(5)
    var =  page.getobjectcout()
    arr = []
    for a in range(1,var):
        url =  page.geturl(a)
        arr.append(url)   
    print(arr)
    header = [ "curl","Categories", "Name", "Baseinfo", "Tel-occupation", "Street-address", "Postal-code", "Locality", "Region", "Link", "E-mail", "Phone", "Portable", "Social Media FB", "Social Media Instagram" ]
    page.write_array_to_excel(header,"array_data.xlsx","Sheet")
    for i in arr:
        rr = []
        page.navigatetopage(i)
        status = page.is_element_present(*PageLocators.categories_FIELD)
        print(status)
        curl = page.current_url()
        rr.append(curl)
        catogriespre = page.getcategories()
        catogries = page.array_to_csv_string(catogriespre)
        rr.append(catogries)
        print(catogries)
        propertyame = page.getName()
        print(propertyame)
        rr.append(propertyame)
        teloccupation = page.getTeloccupation_FIELD()
        print(teloccupation)
        rr.append(teloccupation)
        addressone = page.getAddressone_FIELD()
        print(addressone)
        rr.append(addressone)
        address = page.getAddressFIELD()
        print(address)
        rr.append(address)
        postalcode = page.getPostalCodeFIELD()
        print(postalcode)
        rr.append(postalcode)
        locallity = page.getLocalityFIELD()
        print(locallity)
        rr.append(locallity)
        rejion = page.getRegionFIELD()
        print(rejion)
        rr.append(rejion)
        lik = page.getWeb_FIELD()
        print(lik)
        rr.append(lik)
        email = page.getEmail_FIELD()
        print(email)
        rr.append(email)
        phoe = page.getPhone_FIELD()
        print(phoe)
        rr.append(phoe)
        portable = page.getPortable_FIELD()
        print(portable)
        rr.append(portable)
        socialmedia = page.getSocialMedia_FIELD()
        print(socialmedia)
        rr.append(socialmedia)
        socialmediatwo = page.getSocialMedia_FIELDtwo()
        print(socialmediatwo)
        rr.append(socialmediatwo)
        socialmediathree = page.getSocialMedia_FIELDthree()
        print(socialmediathree)
        rr.append(socialmediathree)
        page.write_array_to_excel(rr,"array_data.xlsx","Sheet")


        



options = uc.ChromeOptions()

# setting profile
options.user_data_dir = str(current_directory)+"/"+profile
options.add_argument('--disable-blink-features=AutomationControlled')
driver = uc.Chrome(executable_path=ChromeDriverManager().install(),options=options)

test_email_login_with_correct_code(driver)
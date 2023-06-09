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
excelfilename = config.get('DEFAULT','excelfilename')
excelsheetname = config.get('DEFAULT','excelsheetname')
who_what_field = config.get('DEFAULT','bar')
where_field = config.get('DEFAULT','zurich')

def test_email_login_with_correct_code(browser):
    page = LoginPage(browser, link)
    page.open()
    page.who_what_field(who_what_field)
    page.where_field(where_field)
    page.click_submit()
    page.pause(5)
    var =  page.getobjectcout()
    arr = []
    for a in range(1,var):
        url =  page.geturl(a)
        arr.append(url)   
    print(len(arr))
    header = [ "currenturl","Categories", "Name", "Baseinfo", "Tel-occupation", "Street-address", "Postal-code", "Locality", "Region", "Link", "E-mail", "Phone", "Portable", "Social Media FB", "Social Media Instagram" ]
    page.write_array_to_excel(header,excelfilename+".xlsx",excelsheetname)
    for i in arr:
        rr = []
        page.navigatetopage(i)
        status = page.is_element_present(*PageLocators.categories_FIELD)
        if(status):
            pass
        else:
            page.pause(3)
        curl = page.current_url()
        rr.append(curl)
        catogriespre = page.getcategories()
        catogries = page.array_to_csv_string(catogriespre)
        rr.append(catogries)
        propertyame = page.getName()
        rr.append(propertyame)
        teloccupation = page.getTeloccupation_FIELD()
        rr.append(teloccupation)
        addressone = page.getAddressone_FIELD()
        rr.append(addressone)
        address = page.getAddressFIELD()
        rr.append(address)
        postalcode = page.getPostalCodeFIELD()
        rr.append(postalcode)
        locallity = page.getLocalityFIELD()
        rr.append(locallity)
        rejion = page.getRegionFIELD()
        rr.append(rejion)
        lik = page.getWeb_FIELD()
        rr.append(lik)
        email = page.getEmail_FIELD()
        rr.append(email)
        phoe = page.getPhone_FIELD()
        rr.append(phoe)
        portable = page.getPortable_FIELD()
        rr.append(portable)
        socialmedia = page.getSocialMedia_FIELD()
        rr.append(socialmedia)
        socialmediatwo = page.getSocialMedia_FIELDtwo()
        rr.append(socialmediatwo)
        socialmediathree = page.getSocialMedia_FIELDthree()
        rr.append(socialmediathree)
        new_array = [s.replace("o value", " ") for s in rr]
        page.write_array_to_excel(new_array,excelfilename+".xlsx",excelsheetname)


        



options = uc.ChromeOptions()

# setting profile
options.user_data_dir = str(current_directory)+"/"+profile
options.add_argument('--disable-blink-features=AutomationControlled')
driver = uc.Chrome(executable_path=ChromeDriverManager().install(),options=options)

test_email_login_with_correct_code(driver)
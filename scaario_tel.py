from pages.locators import PageLocators
from pages.tel_directory import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import os
from webdriver_manager.chrome import ChromeDriverManager

current_directory = os.getcwd()
profile = "search"

def test_email_login_with_correct_code(browser):
    link = "https://tel.search.ch/"
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
    for i in arr:
        page.navigatetopage(i)
        status = page.is_element_present(*PageLocators.categories_FIELD)
        print(status)
        catogries = page.getcategories()
        print(catogries)
        



options = uc.ChromeOptions()

# setting profile
options.user_data_dir = str(current_directory)+"/"+profile
options.add_argument('--disable-blink-features=AutomationControlled')
driver = uc.Chrome(executable_path=ChromeDriverManager().install(),options=options)

test_email_login_with_correct_code(driver)
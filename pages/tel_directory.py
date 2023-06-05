import re
from .base_page import BasePage
from .locators import PageLocators
from selenium.webdriver.common.by import By
import time


class LoginPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)

    def who_what_field(self, keyval):
        Phonenumber = self.browser.find_element(*PageLocators.Phonenumber_INPUT)
        Phonenumber.send_keys(keyval)

    def where_field(self, keyval):
        Phonenumber = self.browser.find_element(*PageLocators.Where_INPUT)
        Phonenumber.send_keys(keyval)
        
    def pause(self, keyval):
        time.sleep(int(keyval))


    def click_submit(self):
        Phonenumber = self.browser.find_element(*PageLocators.Submit_BUTTON)
        Phonenumber.click()

    def geturl(self,index):
        scroll_distance = 5000  # Adjust the distance as needed
        scroll_script = f"window.scrollBy(0, {scroll_distance});"
        self.browser.execute_script(scroll_script)
        xpath = str(PageLocators.Url_FIELD)
        print(xpath)
        full = "("+str(xpath.replace(", ","").replace("xpath","").replace("'","").replace("\\","").replace("(","").replace(")",""))+")["+str(index)+"]"
        print(full)
        urlval = self.browser.find_element(By.XPATH,full)
        try:
            val = urlval.get_attribute("href")
        except:
            val = "not found"
        return val
    

    def getobjectcout(self):
        cout = self.browser.find_element(*PageLocators.Header_title).text
        value = cout.split("entries")[0].replace(" ","")
        try:
            val = int(value)
        except:
            val = 0
        return val

    def navigatetopage(self,url):
        self.browser.get(url)

    def getcategories(self):
        arr = []
        vals = self.browser.find_elements(*PageLocators.categories_FIELD)
        for a in vals:
            try:
                value = a.text
                arr.append(value)
                print(value)
            except:
                value = "o value"
        return arr

    def getName(self):
        val = self.browser.find_element(*PageLocators.Name_FIELD)
        try:
            value = val.text
        except:
            value = "o value"
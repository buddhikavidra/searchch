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
        try:
            urlval = self.browser.find_element(By.XPATH,full)
        except:
            time.sleep(5)
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
        try:
            val = self.browser.find_element(*PageLocators.Name_FIELD)
            value = val.text
            string_without_special_chars = re.sub(r"[^a-zA-Z0-9\s]", "", value.replace("\n", ""))
        except:
            string_without_special_chars = "o value"
        return string_without_special_chars


    def getAddressFIELD(self):
        try:
            vals = self.browser.find_element(*PageLocators.Address_FIELD)
            value = vals.text
        except:
            value = "o value"
        return value   
    
    def getPostalCodeFIELD(self):
        try:
            vals = self.browser.find_element(*PageLocators.PostalCode_FIELD)
            value = vals.text
        except:
            value = "o value"
        return value           

    def getRegionFIELD(self):
        try:
            vals = self.browser.find_element(*PageLocators.Region_FIELD)
            value = vals.text
        except:
            value = "o value"
        return value   

    def getLocalityFIELD(self):
        try:
            vals = self.browser.find_element(*PageLocators.Locality_FIELD)
            value = vals.text
        except:
            value = "o value"
        return value  

    def getDirectionsFIELD(self):
        try:
            vals = self.browser.find_element(*PageLocators.Directions_FIELD)
            value = vals.text
        except:
            value = "o value"
        return value     
          
    def getWeb_FIELD(self):
        try:
            vals = self.browser.find_element(*PageLocators.Link_FIELD)
            value = vals.text
        except:
            value = "o value"
        return value  
    def getEmail_FIELD(self):
        try:
            vals = self.browser.find_element(*PageLocators.Email_FIELDtwo)
            value = vals.get_attribute("href")
        except:
            value = "o value"
        return value  
    def getPhone_FIELD(self):
        try:
            vals = self.browser.find_element(*PageLocators.Phone_FIELD)
            value = vals.text
        except:
            value = "o value"
        return value  
    def getPortable_FIELD(self):
        try:
            vals = self.browser.find_element(*PageLocators.Portable_FIELD)
            value = vals.text
        except:
            value = "o value"
        return value  
    def getSocialMedia_FIELD(self):
        try:
            vals = self.browser.find_element(*PageLocators.SocialMedia_FIELD)
            value = vals.get_attribute("href")
        except:
            value = "o value"
        return value  

    def getSocialMedia_FIELDtwo(self):
        try:
            vals = self.browser.find_element(*PageLocators.SocialMedia_FIELDtwo)
            value = vals.get_attribute("href")
        except:
            value = "o value"
        return value  

    def getSocialMedia_FIELDthree(self):
        try:
            vals = self.browser.find_element(*PageLocators.SocialMedia_FIELDthree)
            value = vals.get_attribute("href")
        except:
            value = "o value"
        return value  
    

    def getAddressone_FIELD(self):
        try:
            vals = self.browser.find_element(*PageLocators.AddressOne_FIELD)
            value = vals.text
        except:
            value = "o value"
        return value  


    def getTeloccupation_FIELD(self):
        try:
            vals = self.browser.find_element(*PageLocators.Teloccupation_FIELD)
            value = vals.text
        except:
            value = "o value"
        return value  
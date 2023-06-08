from selenium.webdriver.common.by import By


class PageLocators():
    Phonenumber_INPUT = (By.XPATH, '//input[@name="was"]')
    Where_INPUT = (By.XPATH, '//input[@name="wo"]')
    Submit_BUTTON = (By.XPATH, '//input[@value="Search"]')  
    Url_FIELD = (By.XPATH, '//ul[@class="tel-result-actions sl-screenonly sl-floatlist"]/parent::td/parent::tr/parent::tbody/descendant::h1/a') 
    Header_title = (By.XPATH,'//h1[@class="sl-card-header-title"]')
    categories_FIELD = (By.XPATH,'//div[@class="tel-categories"]/span/a')
    Name_FIELD = (By.XPATH,'//h1')
    Teloccupation_FIELD = (By.XPATH,'(//div[@class="tel-detail-baseinfo"]/descendant::span[not(@*)])[last()]')
    AddressOne_FIELD = (By.XPATH,'//div[@class="tel-occupation"]')
    Address_FIELD = (By.XPATH,'//span[@class="street-address"]')
    PostalCode_FIELD = (By.XPATH,'//span[@class="postal-code"]')
    Region_FIELD = (By.XPATH,'//span[@class="region"]')
    Locality_FIELD = (By.XPATH,'//span[@class="locality"]')
    BookTable_FIELD = (By.XPATH,"(//a[text()='Book a table'])[1]")
    Directions_FIELD = (By.XPATH,"(//a[text()='Directions'])[1]")
    Web_FIELD = (By.XPATH,"(//a[text()='Web'])[1]")
    Email_FIELD = (By.XPATH,"(//a[text()='E-mail *'])[1]") #//a[@id="tel_email_0"]
    Phone_FIELD = (By.XPATH,"//td[text()='Phone']/parent::tr/descendant::a") 
    Portable_FIELD = (By.XPATH,"//td[text()='Portable']/parent::tr/descendant::a")  
    Email_FIELDtwo = (By.XPATH,"//td[text()='E-mail']/parent::tr/descendant::a") 
    Link_FIELD = (By.XPATH,"//td[text()='Link']/parent::tr/descendant::a")  
    SocialMedia_FIELD = (By.XPATH,"//td[text()='Social Media']/parent::tr/descendant::a[1]")
    SocialMedia_FIELDtwo = (By.XPATH,"//td[text()='Social Media']/parent::tr/descendant::a[2]")
    SocialMedia_FIELDthree = (By.XPATH,"//td[text()='Social Media']/parent::tr/descendant::a[3]")

    
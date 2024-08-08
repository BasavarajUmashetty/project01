from selenium.webdriver.common.by import By
from pom.facebook import facebook
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_Login(self):
        fb=facebook(self.driver)
        fb.getfbuser().send_keys("Basavaraj.Umashetty@gmail.com")
        #print(self.driver.title)

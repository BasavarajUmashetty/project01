from selenium.webdriver.common.by import By


class facebook:

    def __init__(self, driver):
        self.driver = driver

    fbuser = (By.XPATH,"//*[@id='email']")

    def getfbuser(self):
        return self.driver.find_element(*facebook.fbuser)
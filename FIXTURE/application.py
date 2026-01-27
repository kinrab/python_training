
from selenium  import webdriver
from FIXTURE.session import SessionHelper
from FIXTURE.group import GroupHelper
from FIXTURE.contact import ContactHelper

class Application:

    def __init__(self, browser, base_url):

        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        elif browser == "edge":
            self.driver = webdriver.Edge()
        else:
            raise ValueError("Unrecognised browser %s" % browser)

        self.driver.implicitly_wait(5)    #Для учебного приложения это не нужно  - все элементы сразу на странице при открытии получаются...

        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):

        try:
              self.driver.current_url
              return True
        except:
              return False


    def Destroy(self):

        self.driver.quit()
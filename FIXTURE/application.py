
from selenium.webdriver.firefox.webdriver import WebDriver
from FIXTURE.session import SessionHelper
from FIXTURE.group import GroupHelper
from FIXTURE.contact import ContactHelper

class Application:

    def __init__(self):

        self.driver = WebDriver()
        self.driver.implicitly_wait(30)

        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):

        try:
              self.wd.current_url
              return True
        except:
              return False


    def Destroy(self):

        self.driver.quit()
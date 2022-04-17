import string
import random
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class FunctionalTests(StaticLiveServerTestCase):
    # Use a predefined fixture from a test database
    # fixtures = ['masterDatabase.json']

    def testSignUp(self):
        # Go to sign up page
        # Initialise driver
        self.driver = webdriver.Chrome('apps/home/chromedriver')

        # direct the webdriver to where the browser file is:
        # your secret credentials:
        email = "andricozach@gmail.com"
        password = "***REMOVED***"
        # Go to linkedin and login
        self.driver.get('https://www.linkedin.com/login')
        #time.sleep(.5)
        self.driver.find_element_by_id('username').send_keys(email)
        #time.sleep(.5)
        self.driver.find_element_by_id('password').send_keys(password)
        #time.sleep(.5)
        self.driver.find_element_by_id('password').send_keys(Keys.RETURN)
        #time.sleep(1)


        # Go to sign up page
        self.driver.get('https://www.linkedin.com/in/ajrobbins/')
        time.sleep(3)

        aboutSection = self.driver.find_element_by_class_name("pv-shared-text-with-see-more").text
        print(aboutSection)

        # Finish test and quit driver
        self.driver.quit()
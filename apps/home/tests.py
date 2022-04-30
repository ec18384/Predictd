import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from core import settings


class FunctionalTests(StaticLiveServerTestCase):
    # Use a predefined fixture from a test database
    # fixtures = ['masterDatabase.json']

    def testSummaryScrape(self):
        driver = webdriver.Chrome('apps/home/chromedriver')

        # direct the webdriver to where the browser file is:
        # your secret credentials:
        email = settings.LINKEDIN_EMAIL
        password = settings.LINKEDIN_PASSWORD
        # Go to linkedin and login
        driver.get('https://www.linkedin.com/login')
        # time.sleep(.5)
        driver.find_element_by_id('username').send_keys(email)
        # time.sleep(.5)
        driver.find_element_by_id('password').send_keys(password)
        # time.sleep(.5)
        driver.find_element_by_id('password').send_keys(Keys.RETURN)
        # time.sleep(1)

        # Go to sign up page
        driver.get('https://www.linkedin.com/in/andrico')
        time.sleep(3)

        aboutSection = driver.find_elements_by_xpath(xpath="//div[3]/div/div/div/span")

        aboutText = ""

        for elements in aboutSection:
            aboutText += elements.text

        print(aboutText)

        response = aboutText

        # Finish test and quit driver
        driver.quit()

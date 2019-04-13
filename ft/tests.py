from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

class AdminTest(StaticLiveServerTestCase):
    
    fixtures = ['fixtures/admin.json',]

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver.exe')

    def tearDown(self):
        self.browser.quit()

    def test_admin_site(self):
        # user opens web browser, navigates to admin page
        self.browser.get(self.live_server_url + '/admin/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)
        # users types in username and passwords and presses enter
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('admin')
        password_field.send_keys(Keys.RETURN)
        # login credentials are correct, and the user is redirected to the main admin page
        time.sleep(3)
        try:
            body = WebDriverWait(self.browser, 3).until(lambda x: x.find_element_by_tag_name("body"))
            print('page is ready')
        except TimeoutException:
            print('Loading takes too much time')
        self.assertIn('Site administration', body.text)
        # user clicks on the Users link
        user_link = self.browser.find_elements_by_link_text('Users')
        user_link[0].click()
        # user verifies that user live@forever.com is present
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('live@forever.com', body.text)

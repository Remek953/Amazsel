import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from pages.login_page import Login

import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestRegisterPage(unittest.TestCase):

	""" 
	There are 2 ways to visit login site.
	First  - open by main page,  second - open by url.
	"""
	
	def setUp(self):
		options = Options()
		options.add_argument('start-maximized')  
		options.add_argument("--disable-extensions")
		#options.add_argument("--headless") # Runs Chrome in headless mode.
		self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

	def tearDown(self):
		self.driver.close()

	def test_login_page_url(self):
		login_page = Login(self.driver)
		login_page.open_login_page_url()
		login_page.print_title()
		assert login_page.is_title_matches()

	def test_login_page_main(self):
		login_page = Login(self.driver)
		login_page.open_login_page_main()
		login_page.print_title()
		assert login_page.is_title_matches()

	def test_empty_input_url(self):
		login_page = Login(self.driver)
		login_page.open_login_page_url()
		login_page.click_cont_button()
		assert login_page.empty_alert()

	def test_invalid_email_url(self):
		login_page = Login(self.driver)
		login_page.open_login_page_url()
		login_page.set_email_phone_input("test")
		login_page.click_cont_button()
		assert login_page.email_alert()

	def test_invalid_phone_url(self):
		login_page = Login(self.driver)
		login_page.open_login_page_url()
		login_page.set_email_phone_input("999")
		login_page.click_cont_button()
		assert login_page.phone_alert()

	def test_valid_email_url(self):
		login_page = Login(self.driver)
		login_page.open_login_page_url()
		login_page.set_email_phone_input("test@gmail.com")
		login_page.click_cont_button()
		assert login_page.check_valid_email("test@gmail.com")

	def test_check_forgot_pass_url(self):
		login_page = Login(self.driver)
		login_page.open_login_page_url()
		login_page.click_forgot_password_link()
		assert login_page.check_forgot_password_site()

	def test_check_other_issues_url(self):
		login_page = Login(self.driver)
		login_page.open_login_page_url()
		login_page.click_other_issues_link()
		assert login_page.check_other_issues_site()

	def test_create_acc_url(self):
		login_page = Login(self.driver)
		login_page.open_login_page_url()
		login_page.click_create_acc_buttom()
		assert login_page.check_create_acc_site()


if __name__ == "__main__":
	unittest.main()
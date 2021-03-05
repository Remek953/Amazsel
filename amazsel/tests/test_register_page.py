import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from pages.register_page import Register

import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestRegisterPage(unittest.TestCase):

	""" 
	There are 2 different register site.
	First  - open by main page,  second - open by url.
	The first (main page), alerts appear below the placeholder.
	The second (URL), the alert appears at the top of the text of the message box.
	"""
	
	def setUp(self):
		options = Options()
		options.add_argument('start-maximized')  
		options.add_argument("--disable-extensions")
		#options.add_argument("--headless") # Runs Chrome in headless mode.
		self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

	def tearDown(self):
		self.driver.close()

	def test_register_page_url(self):
		register_page = Register(self.driver)
		register_page.open_register_page_url()
		register_page.print_title()
		assert register_page.is_title_matches()

	def test_register_page_main(self):
		register_page = Register(self.driver)
		register_page.open_register_page_main()
		register_page.print_title()
		assert register_page.is_title_matches()

	def test_all_empty_main(self):
		register_page = Register(self.driver)
		register_page.open_register_page_main()
		register_page.click_acc_button()
		assert register_page.name_alert()
		assert register_page.email_alert()
		assert register_page.password_alert()

	def test_name_main(self):
		register_page = Register(self.driver)
		register_page.open_register_page_main()
		register_page.set_name_input("test")
		register_page.click_acc_button()
		assert not register_page.name_alert()
		assert register_page.email_alert()
		assert register_page.password_alert()

	def test_invalid_email_main(self):
		register_page = Register(self.driver)
		register_page.open_register_page_main()
		register_page.set_email_input("test")
		register_page.click_acc_button()
		assert register_page.name_alert()
		assert register_page.invalid_email_alert()
		assert register_page.password_alert()

	def test_valid_email_main(self):
		register_page = Register(self.driver)
		register_page.open_register_page_main()
		register_page.set_email_input("test@test.com")
		register_page.click_acc_button()
		assert register_page.name_alert()
		assert not register_page.email_alert()
		assert register_page.password_alert()

	def test_short_password_main(self):
		register_page = Register(self.driver)
		register_page.open_register_page_main()
		register_page.set_password_input("test")
		register_page.click_acc_button()
		assert register_page.name_alert()
		assert register_page.email_alert()
		assert register_page.short_password_alert()

	def test_valid_password_main(self):
		register_page = Register(self.driver)
		register_page.open_register_page_main()
		register_page.set_password_input("testtest")
		register_page.click_acc_button()
		assert register_page.name_alert()
		assert register_page.email_alert()
		assert not register_page.password_alert()

	def test_re_password_main(self):
		register_page = Register(self.driver)
		register_page.open_register_page_main()
		register_page.set_re_password_input("test")
		register_page.click_acc_button()
		assert register_page.name_alert()
		assert register_page.email_alert()
		assert register_page.password_alert()

	def test_mismatch_short_password_main(self):
		register_page = Register(self.driver)
		register_page.open_register_page_main()
		register_page.set_password_input("test")
		register_page.set_re_password_input("test1")
		register_page.click_acc_button()
		assert register_page.name_alert()
		assert register_page.email_alert()
		assert register_page.short_password_alert()
		assert register_page.re_password_alert_matches()

	def test_mismatch_password_main(self):
		register_page = Register(self.driver)
		register_page.open_register_page_main()
		register_page.set_password_input("testtest1")
		register_page.set_re_password_input("test1")
		register_page.click_acc_button()
		assert register_page.name_alert()
		assert register_page.email_alert()
		assert not register_page.short_password_alert()
		assert register_page.re_password_alert_matches()

	def test_all_empty_url(self):
		register_page = Register(self.driver)
		register_page.open_register_page_url()
		register_page.click_acc_button()
		assert register_page.box_alert()
		assert register_page.box_name_alert_0()
		assert register_page.box_email_alert_0()
		assert register_page.box_password_alert_0()

	def test_name_url(self):
		register_page = Register(self.driver)
		register_page.open_register_page_url()
		register_page.set_name_input("test")
		register_page.click_acc_button()
		assert register_page.box_alert()
		assert not register_page.box_name_alert_0()

	def test_email_url(self):
		register_page = Register(self.driver)
		register_page.open_register_page_url()
		register_page.set_email_input("test")
		register_page.click_acc_button()
		assert register_page.box_alert()
		assert register_page.box_name_alert_0()
		assert register_page.box_invalid_email_alert()
		assert register_page.box_password_alert_0()

	def test_password_url(self):
		register_page = Register(self.driver)
		register_page.open_register_page_url()
		register_page.set_password_input("test")
		register_page.click_acc_button()
		assert register_page.box_alert()
		assert register_page.box_name_alert_0()
		assert register_page.box_email_alert_0()
		assert register_page.box_match_password_alert()
	
	def test_mismatch_password_url(self):
		register_page = Register(self.driver)
		register_page.open_register_page_url()
		register_page.set_password_input("test")
		register_page.set_re_password_input("test1")
		register_page.click_acc_button()
		assert register_page.box_alert()
		assert register_page.box_name_alert_0()
		assert register_page.box_email_alert_0()
		assert register_page.box_match_password_alert()

if __name__ == "__main__":
	unittest.main()
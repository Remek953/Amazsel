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
	
	def setUp(self):
		options = Options() 
		#options.add_argument("--profile-directory=Default")
		#options.add_argument("--user-data-dir=selenium")
		options.add_argument('start-maximized')  
		options.add_argument("--disable-extensions")
		#options.add_argument("--headless") # Runs Chrome in headless mode.
		#options.add_argument("--no-sandbox") # Bypass OS security model
		#options.add_argument('disable-infobars')
		#options.add_argument('--disable-gpu')
		#options.add_argument('--incognito')
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


if __name__ == "__main__":
	unittest.main()
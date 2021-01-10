import sys
import os
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from selenium.webdriver.common.keys import Keys
from pages.main_page import MainPage
import time

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class TestMainPage(unittest.TestCase):

	def setUp(self):
		chrome_options = Options()
		chrome_options.add_argument("--headless")
		chrome_options.add_argument('--no-sandbox')
		self.driver = webdriver.Chrome(ChromeDriverManager().install())

	def test_main_page(self):
		main_page = MainPage(self.driver)
		main_page.open_page()
		assert main_page.is_title_matches()
		main_page.print_title()
		

if __name__ == "__main__":
	unittest.main()
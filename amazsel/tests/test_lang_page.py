import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from locators.locators import LangPageLocators
from pages.lang_page import LangPage

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



class TestMainPage(unittest.TestCase):

	def setUp(self):
		chrome_options = Options()
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--no-sandbox")
		self.driver = webdriver.Chrome(ChromeDriverManager().install())
		self.driver.maximize_window()

	def test_lang_page(self):
		lang_page = LangPage(self.driver)
		lang_page.open_lang_page()
		assert lang_page.is_lang_title_matches()
		lang_page.print_title()

	def test_esp_lang_page(self):
		lang_page = LangPage(self.driver)
		lang_page.open_lang_page()
		lang_page.click_espanol_check()
		assert lang_page.esp_text_matches()

	def test_eng_lang_page(self):
		lang_page = LangPage(self.driver)
		lang_page.open_lang_page()
		lang_page.click_espanol_check()
		lang_page.click_english_check()
		assert lang_page.eng_text_matches()
		
	def tearDown(self):
		self.driver.close()
		

if __name__ == "__main__":
	unittest.main()
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from locators.locators import LangPageLocators
from pages.lang_page import LangPage

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestLangPage(unittest.TestCase):

	"""
	Add default profile because
	detect all the checkbox and dropdown menu
	(all the language and currency menu)
	"""
	
	def setUp(self):
		options = Options() 
		options.add_argument("--profile-directory=Default")
		options.add_argument("--user-data-dir=selenium")
		options.add_argument('start-maximized')  
		options.add_argument("--disable-extensions")
		#options.add_argument("--headless") # Runs Chrome in headless mode.
		self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

	def tearDown(self):
		self.driver.close()

	def test_lang_page(self):
		lang_page = LangPage(self.driver)
		lang_page.open_lang_page()
		assert lang_page.is_lang_title_matches()
		lang_page.print_title()

	def test_esp_lang_page(self):
		lang_page = LangPage(self.driver)
		lang_page.open_lang_page()
		lang_page.click_espanol_check()
		assert lang_page.espanol_lang_matches()

	def test_eng_lang_page(self):
		lang_page = LangPage(self.driver)
		lang_page.open_lang_page()
		lang_page.click_espanol_check()
		lang_page.click_english_check()
		assert lang_page.english_lang_matches()

	def test_de_lang_page(self):
		lang_page = LangPage(self.driver)
		lang_page.open_lang_page()
		lang_page.click_deutsch_check()
		assert lang_page.deutsch_lang_matches()

	def test_pt_lang_page(self):
		lang_page = LangPage(self.driver)
		lang_page.open_lang_page()
		lang_page.click_portugues_check()
		assert lang_page.portugues_lang_matches()

	def test_currency_usd(self):
		lang_page = LangPage(self.driver)
		lang_page.open_lang_page()
		lang_page.currency_usd()
		assert lang_page.usd_text_matches

	def test_currency_peso(self):
		lang_page = LangPage(self.driver)
		lang_page.open_lang_page()
		lang_page.currency_peso()
		assert lang_page.peso_text_matches

	def test_currency_euro(self):
		lang_page = LangPage(self.driver)
		lang_page.open_lang_page()
		lang_page.currency_euro()
		assert lang_page.euro_text_matches()

	def test_currency_hong(self):
		lang_page = LangPage(self.driver)
		lang_page.open_lang_page()
		lang_page.currency_hong()
		assert lang_page.hong_text_matches()

	def test_currency_nok(self):
		lang_page = LangPage(self.driver)
		lang_page.open_lang_page()
		lang_page.currency_nok()
		assert lang_page.nok_text_matches()

	def test_currency_pound(self):
		lang_page = LangPage(self.driver)
		lang_page.open_lang_page()
		lang_page.currency_pound()
		assert lang_page.pound_text_matches()

	def test_currency_vnd(self):
		lang_page = LangPage(self.driver)
		lang_page.open_lang_page()
		lang_page.currency_vnd()
		assert lang_page.vnd_text_matches()


if __name__ == "__main__":
	unittest.main()
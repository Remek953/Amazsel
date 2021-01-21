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

from locators.locators import MainPageLocators


class TestMainPage(unittest.TestCase):

	def setUp(self):
		chrome_options = Options()
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--no-sandbox")
		self.driver = webdriver.Chrome(ChromeDriverManager().install())
		self.driver.maximize_window()

	def test_main_page(self):
		main_page = MainPage(self.driver)
		main_page.open_page()
		assert main_page.is_title_matches()
		main_page.print_title()

	def test_click_logo(self):
		main_page = MainPage(self.driver)
		main_page.open_page()
		main_page.click_logo()
		assert main_page.is_title_matches()
		assert main_page.is_logo_url_matches()

	def test_click_desktop_grid_1(self):
		main_page = MainPage(self.driver)
		main_page.open_page()
		title = main_page.check_title_grid_1()
		main_page.click_desktop_grid_1()
		main_page.matches_title_grid(title)
		
	def test_click_desktop_grid_2(self):
		main_page = MainPage(self.driver)
		main_page.open_page()
		title = main_page.check_title_grid_2()
		main_page.click_desktop_grid_2()
		main_page.matches_title_grid(title)
		
	def test_click_desktop_grid_3(self):
		main_page = MainPage(self.driver)
		main_page.open_page()
		title = main_page.check_title_grid_3()
		main_page.click_desktop_grid_3()
		main_page.matches_title_grid(title)
		
	def test_click_desktop_grid_4(self):
		main_page = MainPage(self.driver)
		main_page.open_page()
		title = main_page.check_title_grid_4()
		main_page.click_desktop_grid_4()
		main_page.matches_title_grid(title)
		
	def test_click_desktop_grid_5(self):
		main_page = MainPage(self.driver)
		main_page.open_page()
		title = main_page.check_title_grid_5()
		main_page.click_desktop_grid_5()
		main_page.matches_title_grid(title)
		
	def test_click_desktop_grid_6(self):
		main_page = MainPage(self.driver)
		main_page.open_page()
		title = main_page.check_title_grid_6()
		main_page.click_desktop_grid_6()
		main_page.matches_title_grid(title)
		
	def test_click_desktop_grid_7(self):
		main_page = MainPage(self.driver)
		main_page.open_page()
		title = main_page.check_title_grid_7()
		main_page.click_desktop_grid_7()
		main_page.matches_title_grid(title)

	def test_click_desktop_grid_1_d2(self):
		main_page = MainPage(self.driver)
		main_page.open_page()
		main_page.click_desktop_grid_1_d2()
		header_text = "Amazon.com ships worldwide"
		assert header_text in self.driver.find_element(*MainPageLocators.TITLE_SHIPS_WORLDWIDE).text

	def test_click_desktop_btf_1(self):
		main_page = MainPage(self.driver)
		main_page.open_page()
		main_page.click_desktop_btf_1()
		header_text = "The Women's Shop"
		assert header_text in self.driver.find_element(*MainPageLocators.TITLE_COMFY_STYLES).text

	def test_click_desktop_btf_2(self):
		main_page = MainPage(self.driver)
		main_page.open_page()
		main_page.click_desktop_btf_2()
		header_text = "Computers & Tablets"
		assert header_text in self.driver.find_element(*MainPageLocators.TITLE_LAPTOP_TABLETS).text

	def test_click_desktop_btf_3(self):
		main_page = MainPage(self.driver)
		main_page.open_page()
		main_page.click_desktop_btf_3()
		header_text = "Home bedding"
		assert header_text in self.driver.find_element(*MainPageLocators.TITLE_HOME_BEDDING).text

	def test_click_desktop_btf_4(self):
		main_page = MainPage(self.driver)
		main_page.open_page()
		main_page.click_desktop_btf_4()
		header_text = "strip lighting"
		assert header_text in self.driver.find_element(*MainPageLocators.TITLE_STRIP_LIGHTS).text

	def tearDown(self):
		self.driver.close()
		

if __name__ == "__main__":
	unittest.main()
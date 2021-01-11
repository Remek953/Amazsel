import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from locators.locators import MainPageLocators

class MainPage:

	def __init__(self, driver):
		self.driver = driver
	def open_page(self):
		self.driver.get("https://www.amazon.com/")
	def is_title_matches(self):
		return "Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more" in self.driver.title
	def print_title(self):
		print(self.driver.title)
	def click_logo(self):
		self.driver.find_element(*MainPageLocators.LOGO).click()
	def is_logo_url_matches(self):
		return "https://www.amazon.com/ref=nav_logo" in self.driver.current_url



	
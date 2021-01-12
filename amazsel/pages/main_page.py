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
		self.driver.implicitly_wait(5)
	def is_title_matches(self):
		return "Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more" in self.driver.title
	def print_title(self):
		print(self.driver.title)
	def click_logo(self):
		self.driver.find_element(*MainPageLocators.LOGO).click()
	def is_logo_url_matches(self):
		return "https://www.amazon.com/ref=nav_logo" in self.driver.current_url
	def click_desktop_grid_1(self):
		self.driver.find_element(*MainPageLocators.DESKTOP_GRID_1).click()
	def click_desktop_grid_2(self):
		self.driver.find_element(*MainPageLocators.DESKTOP_GRID_2).click()
	def click_desktop_grid_3(self):
		self.driver.find_element(*MainPageLocators.DESKTOP_GRID_3).click()
	def click_desktop_grid_4(self):
		self.driver.find_element(*MainPageLocators.DESKTOP_GRID_4).click()
	def click_desktop_grid_5(self):
		self.driver.find_element(*MainPageLocators.DESKTOP_GRID_5).click()
	def click_desktop_grid_6(self):
		self.driver.find_element(*MainPageLocators.DESKTOP_GRID_6).click()
	def click_desktop_grid_7(self):
		self.driver.find_element(*MainPageLocators.DESKTOP_GRID_7).click()
	def click_desktop_grid_8(self):
		self.driver.find_element(*MainPageLocators.DESKTOP_GRID_8).click()





	
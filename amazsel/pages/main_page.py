import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from locators.locators import MainPageLocators
from .base_page import BasePage

class MainPage(BasePage):

	def open_page(self):
		self.driver.get("https://www.amazon.com/")
	def is_title_matches(self):
		return "Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more" in self.driver.title
	def print_title(self):
		print(self.driver.title)
	def click_logo(self):
		self.wait_to_be_clickable(MainPageLocators.LOGO).click()
	def is_logo_url_matches(self):
		return "https://www.amazon.com/ref=nav_logo" in self.driver.current_url

	def click_desktop_grid_1(self):
		self.wait_to_be_clickable(MainPageLocators.DESKTOP_GRID_1).click()
	def click_desktop_grid_2(self):
		self.wait_to_be_clickable(MainPageLocators.DESKTOP_GRID_2).click()
	def click_desktop_grid_3(self):
		self.wait_to_be_clickable(MainPageLocators.DESKTOP_GRID_3).click()
	def click_desktop_grid_4(self):
		self.wait_to_be_clickable(MainPageLocators.DESKTOP_GRID_4).click()
	def click_desktop_grid_5(self):
		self.wait_to_be_clickable(MainPageLocators.DESKTOP_GRID_5).click()
	def click_desktop_grid_6(self):
		self.wait_to_be_clickable(MainPageLocators.DESKTOP_GRID_6).click()
	def click_desktop_grid_7(self):
		self.wait_to_be_clickable(MainPageLocators.DESKTOP_GRID_7).click()

	def check_title_grid(self, locator):
			current_title = self.wait_for_element(locator).text
			if current_title == "AmazonBasics":
				return "'amazonbasics'"
			elif current_title == "Shop by Category":
				return "International Best Sellers"
			elif current_title == "Electronics":
				return "Electronics"
			elif current_title == "Computers & Accessories":
				return "Computers, Tablets and IT Accessories"
			elif current_title == "Shop top categories":
				return "Shop top categories"
			elif current_title == "Beauty picks":
				return "Beauty and Personal Care"
			elif current_title == "Find your ideal TV":
				return current_title == "Television & Video"
			elif current_title == "Get fit at home":
				return "Sports and Outdoors"
			elif current_title == "Deals & Promotions":
				return "Deals and Promotions"
			elif current_title == "Easy returns":
				return "International Returns"

	def check_title_grid_1(self):
		return self.check_title_grid(MainPageLocators.TITLE_GRID_1)
	def check_title_grid_2(self):
		return self.check_title_grid(MainPageLocators.TITLE_GRID_2)
	def check_title_grid_3(self):
		return self.check_title_grid(MainPageLocators.TITLE_GRID_3)
	def check_title_grid_4(self):
		return self.check_title_grid(MainPageLocators.TITLE_GRID_4)
	def check_title_grid_5(self):
		return self.check_title_grid(MainPageLocators.TITLE_GRID_5)
	def check_title_grid_6(self):
		return self.check_title_grid(MainPageLocators.TITLE_GRID_6)
	def check_title_grid_7(self):
		return self.check_title_grid(MainPageLocators.TITLE_GRID_7)

	def matches_title_grid(self, title):
		if title == "AmazonBasics":
			return self.wait_for_element(MainPageLocators.TITLE_AMAZONBASIC).text == title
		elif title == "Shop by Category":
			return self.wait_for_element(MainPageLocators.TITLE_SHOP_BY_CAT).text == title
		elif title == "Electronics":
			return self.wait_for_element(MainPageLocators.TITLE_ELECTRONICS).text == title
		elif title == "Computers & Accessories":
			return self.wait_for_element(MainPageLocators.TITLE_COMPUTERS_ACCESSORIES).text == title
		elif title == "Shop top categories":
			return self.wait_for_element(MainPageLocators.TITLE_SHOP_TOP).text == title
		elif title == "Beauty picks":
			return self.wait_for_element(MainPageLocators.TITLE_BEUATY_PICKS).text == title
		elif title == "Find your ideal TV":
			return self.wait_for_element(MainPageLocators.TITLE_IDEAL_TV).text == title
		elif title == "Get fit at home":
			return self.wait_for_element(MainPageLocators.TITLE_GET_FIT).text == title
		elif title == "Deals & Promotions":
			return self.wait_for_element(MainPageLocators.TITLE_DEALS_PROM).text == title
		elif title == "Easy returns":
			return self.wait_for_element(MainPageLocators.TITLE_EASY_RETURNS).text == title

	def click_desktop_grid_1_d2(self):
		self.wait_to_be_clickable(MainPageLocators.DESKTOP_GRID_1_D2).click()
	def click_desktop_btf_1(self):
		self.wait_to_be_clickable(MainPageLocators.DESKTOP_BTF_GRID_1).click()
	def click_desktop_btf_2(self):
		self.wait_to_be_clickable(MainPageLocators.DESKTOP_BTF_GRID_2).click()
	def click_desktop_btf_3(self):
		self.wait_to_be_clickable(MainPageLocators.DESKTOP_BTF_GRID_3).click()
	def click_desktop_btf_4(self):
		self.wait_to_be_clickable(MainPageLocators.DESKTOP_BTF_GRID_4).click()

	def scroll_down(self):
		self.driver.execute_script("window.scrollTo(0, 3750);")
	def click_back_to_top(self):
		self.wait_to_be_clickable(MainPageLocators.BACK_TO_TOP).click()

	def scroll_down_bottom(self):
		self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	def click_logo_bottom(self):
		self.wait_to_be_clickable(MainPageLocators.LOGO_BOTTOM).click()
	def is_logo_bottom_url_matches(self):
		return "https://www.amazon.com/ref=footer_logo" in self.driver.current_url

	def top_displayed(self):
		if self.wait_for_element(MainPageLocators.TITLE_GRID_1):
			return True
		return False

	def open_lang_change(self):
		self.wait_to_be_clickable(MainPageLocators.LANG_CHANGE).click()
	def is_lang_title_matches(self):
		return "Change Language & Currency Settings" in self.driver.title

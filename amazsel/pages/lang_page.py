import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators.locators import LangPageLocators
from .base_page import BasePage


class LangPage(BasePage):

	def open_lang_page(self):
		self.driver.get("https://www.amazon.com/gp/customer-preferences/")
	def is_lang_title_matches(self):
		return "Change Language & Currency Settings" in self.driver.title
	def print_title(self):
		print(self.driver.title)
	def click_espanol_check(self):
		self.wait_to_be_clickable(LangPageLocators.ESPANOL_CHECK).click()
	def click_english_check(self):
		self.wait_to_be_clickable(LangPageLocators.ENGLISH_CHECK).click()

	def esp_text_matches(self):
		element = self.wait_for_element(LangPageLocators.TEXT_BOX).text
		body_text =  "Traduciremos la información más importante para tu navegación, compras y comunicaciones."
		if body_text in element:
			return True
		return False
	def eng_text_matches(self):
		element = self.wait_for_element(LangPageLocators.TEXT_BOX).text
		body_text =  "We'll translate the most important information for your browsing, shopping, and communications."
		if body_text in element:
			return True
		return False



		
	

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from locators.locators import LangPageLocators
from .base_page import BasePage


class LangPage(BasePage):

	def open_lang_page(self):
		url = "https://www.amazon.com/gp/customer-preferences/"
		self.driver.get(url)
		self.wait_to_be_clickable(LangPageLocators.CANCEL_BUTTON).click()
		self.driver.get(url)
	def is_lang_title_matches(self):
		return "Change Language & Currency Settings" in self.driver.title
	def print_title(self):
		print(self.driver.title)
		
	def click_espanol_check(self):
		self.wait_to_be_clickable(LangPageLocators.ESPANOL_CHECK).click()
	def click_english_check(self):
		self.wait_to_be_clickable(LangPageLocators.ENGLISH_CHECK).click()
	def click_deutsch_check(self):
		self.wait_to_be_clickable(LangPageLocators.DEUTSCH_CHECK).click()
	def click_portugues_check(self):
		self.wait_to_be_clickable(LangPageLocators.PORTUGUES_CHECK).click()

	def espanol_lang_matches(self):
		text = "Traduciremos la información más importante para tu navegación, compras y comunicaciones."
		return text in self.wait_for_element(LangPageLocators.TEXT_BOX).text 
	def english_lang_matches(self):
		text = "We'll translate the most important information for your browsing, shopping, and communications."
		return text in self.wait_for_element(LangPageLocators.TEXT_BOX).text 
	def deutsch_lang_matches(self):
		text = "Die wichtigsten Informationen zu Ihren Suchen, Einkäufen und zu ihrer Kommunikation werden übersetzt."
		return text in self.wait_for_element(LangPageLocators.TEXT_BOX).text 
	def portugues_lang_matches(self):
		text = "Vamos traduzir as informações mais importantes para sua navegação, compras e comunicações."
		return text in self.wait_for_element(LangPageLocators.TEXT_BOX).text 

	def currency_usd(self):
		self.wait_for_element(LangPageLocators.CURRENCY_SET).click()
		self.wait_for_element(LangPageLocators.USD).click()
	def currency_peso(self):
		self.wait_for_element(LangPageLocators.CURRENCY_SET).click()
		self.wait_for_element(LangPageLocators.ARS).click()
	def currency_euro(self):
		self.wait_for_element(LangPageLocators.CURRENCY_SET).click()
		self.wait_for_element(LangPageLocators.EURO).click()
	def currency_hong(self):
		self.wait_for_element(LangPageLocators.CURRENCY_SET).click()
		self.wait_for_element(LangPageLocators.HONG_KONG).click()
	def currency_nok(self):
		self.wait_for_element(LangPageLocators.CURRENCY_SET).click()
		self.wait_for_element(LangPageLocators.NOK).click()
	def currency_pound(self):
		self.wait_for_element(LangPageLocators.CURRENCY_SET).click()
		self.wait_for_element(LangPageLocators.POUNDS).click()
	def currency_vnd(self):
		self.wait_for_element(LangPageLocators.CURRENCY_SET).click()
		self.wait_for_element(LangPageLocators.VND).click()

	def usd_text_matches(self):
		text = ""
		return text == self.wait_for_element(LangPageLocators.CURRENCY_TEXT).text 
	def peso_text_matches(self):
		text = "Note: You will be shown prices in ARS - Argentine Peso on www.amazon.com as a reference only."
		return text in self.wait_for_element(LangPageLocators.CURRENCY_TEXT).text 
	def euro_text_matches(self):
		text = "Note: You will be shown prices in € - EUR - Euro on www.amazon.com as a reference only."
		return text in self.wait_for_element(LangPageLocators.CURRENCY_TEXT).text 
	def hong_text_matches(self):
		text = "Note: You will be shown prices in HK$ - HKD - Hong Kong Dollar on www.amazon.com as a reference only."
		return text in self.wait_for_element(LangPageLocators.CURRENCY_TEXT).text 
	def nok_text_matches(self):
		text = "Note: You will be shown prices in NOK - Norwegian Krone on www.amazon.com as a reference only."
		return text in self.wait_for_element(LangPageLocators.CURRENCY_TEXT).text 
	def pound_text_matches(self):
		text = "Note: You will be shown prices in £ - GBP - Pounds on www.amazon.com as a reference only."
		return text in self.wait_for_element(LangPageLocators.CURRENCY_TEXT).text 
	def vnd_text_matches(self):
		text = "Note: You will be shown prices in ₫ - VND - Vietnamese Dong on www.amazon.com as a reference only."
		return text in self.wait_for_element(LangPageLocators.CURRENCY_TEXT).text 


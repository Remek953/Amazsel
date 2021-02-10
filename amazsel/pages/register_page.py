import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators.locators import RegisterPageLocators
from .base_page import BasePage


class Register(BasePage):

	def open_register_page_url(self):
		url = "https://track.amazon.com/register"
		self.driver.get(url)
	def open_register_page_main(self):
		url = "https://www.amazon.com/"
		self.driver.get(url)
		menu = self.wait_for_element(RegisterPageLocators.DROP_MENU)
		register = self.wait_for_element(RegisterPageLocators.SIGN_UP)
		action = ActionChains(self.driver)
		action.move_to_element(menu).move_to_element(register).click().perform()
	def print_title(self):
		print(self.driver.title)
	def is_title_matches(self):
		return "Amazon Registration" in self.driver.title

		
		
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

	def name_alert(self):
		text = "Enter your name"
		return text in self.wait_for_element(RegisterPageLocators.NAME_ALERT).text 
	def email_alert(self):
		text = "Enter your email"
		return text in self.wait_for_element(RegisterPageLocators.EMAIL_ALERT).text
	def invalid_email_alert(self):
		text = "Enter a valid email address"
		return text in self.wait_for_element(RegisterPageLocators.INVALID_EMAIL_ALERT).text  
	def password_alert(self):
		text = "Enter your password"
		return text in self.wait_for_element(RegisterPageLocators.PASSWORD_ALERT).text 
	def short_password_alert(self):
		text = "Passwords must be at least 6 characters."
		return text in self.wait_for_element(RegisterPageLocators.SHORT_PASSWORD_ALERT).text 
	def re_password_alert(self):
		text = "Type your password again"
		return text in self.wait_for_element(RegisterPageLocators.RE_PASSWORD_ALERT).text 
	def re_password_alert_matches(self):
		text = "Passwords must match"
		return text in self.wait_for_element(RegisterPageLocators.MISMATCH_PASSWORD_ALERT).text 
	def click_acc_button(self):
		self.wait_to_be_clickable(RegisterPageLocators.CREATE_ACC_BUTTON).click()

	def box_alert(self):
		text = "There was a problem"
		return text in self.wait_for_element(RegisterPageLocators.BOX_PROBLEM_ALERT).text 
	def box_name_alert_0(self):
		text = "Enter your name"
		return text in self.wait_for_element(RegisterPageLocators.BOX_NAME_ALERT_0).text 
	def box_email_alert_0(self):
		text = "Enter your email"
		return text in self.wait_for_element(RegisterPageLocators.BOX_EMAIL_ALERT_0).text 
	def box_password_alert_0(self):
		text = "Enter your password"
		return text in self.wait_for_element(RegisterPageLocators.BOX_PASSWORD_ALERT_0).text 

	def set_name_input(self, name):
		self.wait_for_element(RegisterPageLocators.NAME_INPUT).click()
		self.wait_for_element(RegisterPageLocators.NAME_INPUT).send_keys(name)
	def set_email_input(self, email):
		self.wait_for_element(RegisterPageLocators.EMAIL_INPUT).click()
		self.wait_for_element(RegisterPageLocators.EMAIL_INPUT).send_keys(email)
	def set_password_input(self, password):
		self.wait_for_element(RegisterPageLocators.PASSWORD_INPUT).click()
		self.wait_for_element(RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
	def set_re_password_input(self, re_password):
		self.wait_for_element(RegisterPageLocators.RE_PASSWORD_INPUT).click()
		self.wait_for_element(RegisterPageLocators.RE_PASSWORD_INPUT).send_keys(re_password)

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators.locators import LoginPageLocators
from locators.locators import RegisterPageLocators
from .base_page import BasePage


class Login(BasePage):

	def open_login_page_url(self):
		url = "https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=usflex&openid."\
		"claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs."\
		"openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2."\
		"0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2F"\
		"www.amazon.com%2Fgp%2Fcss%2Fhomepage.html%3Fie%3DUTF8%26%252AVersion%252A%3D1%26%252Aentries%252A%3D0"
		self.driver.get(url)
	def open_login_page_main(self):
		url = "https://www.amazon.com/"
		self.driver.get(url)
		menu = self.wait_for_element(RegisterPageLocators.DROP_MENU) #The same locator
		login = self.wait_for_element(LoginPageLocators.SIGN_IN)
		action = ActionChains(self.driver)
		action.move_to_element(menu).move_to_element(login).click().perform()
	def print_title(self):
		print(self.driver.title)
	def is_title_matches(self):
		return "Amazon Sign-In" in self.driver.title
		
	def click_cont_button(self):
		self.wait_to_be_clickable(LoginPageLocators.CONTINUE_BUTTON).click()
	def click_need_help_link(self):
		self.wait_to_be_clickable(LoginPageLocators.NEED_HELP_LINK).click()
	def click_forgot_pass_link(self):
		self.wait_to_be_clickable(LoginPageLocators.FORGOT_PASS_LINK).click()
	def click_other_issues_link(self):
		self.wait_to_be_clickable(LoginPageLocators.OTHER_ISSUES_LINK).click()
	def click_create_acc_buttom(self):
		self.wait_to_be_clickable(LoginPageLocators.CREATE_ACC_BUTTON).click()

	def empty_alert(self):
		text = "Enter your email or mobile phone number"
		return text in self.wait_for_element(LoginPageLocators.EMPTY_EMAIL_PHONE).text 
	def email_alert(self):
		text = "We cannot find an account with that email address"
		return text in self.wait_for_element(LoginPageLocators.EMAIL_PHONE_ALERT).text 
	def phone_alert(self):
		text = "We cannot find an account with that mobile number"
		return text in self.wait_for_element(LoginPageLocators.EMAIL_PHONE_ALERT).text 

	def set_email_phone_input(self, text):
		self.wait_for_element(LoginPageLocators.EMAIL_PHONE_INPUT).click()
		self.wait_for_element(LoginPageLocators.EMAIL_PHONE_INPUT).send_keys(text)

	def click_forgot_password_link(self):
		self.wait_for_element(LoginPageLocators.NEED_HELP_LINK).click()
		self.wait_for_element(LoginPageLocators.FORGOT_PASS_LINK).click()
	def click_other_issues_link(self):
		self.wait_for_element(LoginPageLocators.NEED_HELP_LINK).click()
		self.wait_for_element(LoginPageLocators.OTHER_ISSUES_LINK).click()

	def check_valid_email(self, text):
		return text in self.wait_for_element(LoginPageLocators.VALID_EMAIL).text 
	def check_forgot_password_site(self):
		text = "Password assistance"
		return text in self.wait_for_element(LoginPageLocators.FORGOT_PASS_SITE).text 
	def check_other_issues_site(self):
		text = "Account & Login Issues"
		return text in self.wait_for_element(LoginPageLocators.OTHER_ISSUES_SITE).text 
	def check_create_acc_site(self):
		text = "Create account"
		return text in self.wait_for_element(LoginPageLocators.CREATE_ACC_SITE).text 




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LocatorType:
	CLASS_NAME = 'class name'
	CSS_SELECTOR = 'css selector'
	ID = 'id'
	LINK_TEXT = 'link text'
	NAME = 'name'
	XPATH = 'xpath'

class BasePage(object):
	
	def __init__(self, driver):
		self.driver = driver

	def wait_for_element(self, locator, timeout = 5):
		element = None

		if locator[0] == LocatorType.CLASS_NAME:
			try:
				element = WebDriverWait(self.driver, timeout).until(
						EC.presence_of_element_located((By.CLASS_NAME, locator[1])))
			except TimeoutException as ex:
				print ("Loading took too much time or not found CLASS NAME element")

		elif locator[0] == LocatorType.CSS_SELECTOR:
			try:
				element = WebDriverWait(self.driver, timeout).until(
					EC.presence_of_element_located((By.CSS_SELECTOR, locator[1])))
			except TimeoutException as ex:
				print ("Loading took too much time or not found CSS SELECTOR element")

		elif locator[0] == LocatorType.ID:
			try:
				element = WebDriverWait(self.driver, timeout).until(
					EC.presence_of_element_located((By.ID, locator[1])))
			except TimeoutException as ex:
				print ("Loading took too much time or not found ID element")

		elif locator[0] == LocatorType.LINK_TEXT:
			try:
				element = WebDriverWait(self.driver, timeout).until(
					EC.presence_of_element_located((By.LINK_TEXT, locator[1])))
			except TimeoutException as ex:
				print ("Loading took too much time or not found LINK TEXT element")

		elif locator[0] == LocatorType.NAME:
			try:
				element = WebDriverWait(self.driver, timeout).until(
					EC.presence_of_element_located((By.NAME, locator[1])))
			except TimeoutException as ex:
				print ("Loading took too much time or not found NAME element")

		elif locator[0] == LocatorType.XPATH:
			try:
				element = WebDriverWait(self.driver, timeout).until(
					EC.presence_of_element_located((By.XPATH, locator[1])))
			except TimeoutException as ex:
				print ("Loading took too much time or not found XPATH element")

		else:
				print("Locator not found")
		return element

	def wait_to_be_clickable(self, locator, timeout = 5):
		element = None

		if locator[0] == LocatorType.CLASS_NAME:
			try:
				element = WebDriverWait(self.driver, timeout).until(
						EC.element_to_be_clickable((By.CLASS_NAME, locator[1])))
			except TimeoutException as ex:
				print ("Loading took too much time or not found CLASS NAME element")

		elif locator[0] == LocatorType.CSS_SELECTOR:
			try:
				element = WebDriverWait(self.driver, timeout).until(
					EC.element_to_be_clickable((By.CSS_SELECTOR, locator[1])))
			except TimeoutException as ex:
				print ("Loading took too much time or not found CSS SELECTOR element")

		elif locator[0] == LocatorType.ID:
			try:
				element = WebDriverWait(self.driver, timeout).until(
					EC.element_to_be_clickable((By.ID, locator[1])))
			except TimeoutException as ex:
				print ("Loading took too much time or not found ID element")

		elif locator[0] == LocatorType.LINK_TEXT:
			try:
				element = WebDriverWait(self.driver, timeout).until(
					EC.element_to_be_clickable((By.LINK_TEXT, locator[1])))
			except TimeoutException as ex:
				print ("Loading took too much time or not found LINK TEXT element")

		elif locator[0] == LocatorType.NAME:
			try:
				element = WebDriverWait(self.driver, timeout).until(
					EC.element_to_be_clickable((By.NAME, locator[1])))
			except TimeoutException as ex:
				print ("Loading took too much time or not found NAME element")

		elif locator[0] == LocatorType.XPATH:
			try:
				element = WebDriverWait(self.driver, timeout).until(
					EC.element_to_be_clickable((By.XPATH, locator[1])))
			except TimeoutException as ex:
				print ("Loading took too much time or not found XPATH element")

		else:
				print("Locator not found")
		return element
    
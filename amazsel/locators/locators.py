from selenium.webdriver.common.by import By

class MainPageLocators:
	LOGO_URL = 'https://www.amazon.com/ref=nav_logo'
	LOGO = (By.ID, "nav-logo-sprites")
	# The hrefs below in the first small images when page loads
	DESKTOP_GRID_1 = (By.XPATH, "//*[@id='desktop-grid-1']/div/div[3]/a")
	DESKTOP_GRID_2 = (By.XPATH, "//*[@id='desktop-grid-2']/div/div[3]/a")
	DESKTOP_GRID_3 = (By.XPATH, "//*[@id='desktop-grid-3']/div/div[3]/a")
	DESKTOP_GRID_4 = (By.XPATH, "//*[@id='desktop-grid-4']/div/div[3]/a")
	DESKTOP_GRID_5 = (By.XPATH, "//*[@id='desktop-grid-5']/div/div[3]/a")
	DESKTOP_GRID_6 = (By.XPATH, "//*[@id='desktop-grid-6']/div/div[3]/a")
	DESKTOP_GRID_7 = (By.XPATH, "//*[@id='desktop-grid-7']/div/div[3]/a")
	DESKTOP_GRID_1_D2 = (By.CSS_SELECTOR, "img[alt='We ship 45 million products around the world']")
	# The hrefs below in the 4 small images in the middle
	DESKTOP_BTF_GRID_1 = (By.XPATH, "//*[@id='desktop-btf-grid-1']/div/div[3]/a")
	DESKTOP_BTF_GRID_2 = (By.XPATH, "//*[@id='desktop-btf-grid-2']/div/div[3]/a")
	DESKTOP_BTF_GRID_3 = (By.XPATH, "//*[@id='desktop-btf-grid-3']/div/div[3]/a")
	DESKTOP_BTF_GRID_4 = (By.XPATH, "//*[@id='desktop-btf-grid-4']/div/div[3]/a")
	# Top title text in the first 7 small img when page loads
	TITLE_GRID_1 = (By.XPATH, "//*[@id='desktop-grid-1']/div/div[1]/h2")
	TITLE_GRID_2 = (By.XPATH, "//*[@id='desktop-grid-2']/div/div[1]/h2")
	TITLE_GRID_3 = (By.XPATH, "//*[@id='desktop-grid-3']/div/div[1]/h2")
	TITLE_GRID_4 = (By.XPATH, "//*[@id='desktop-grid-4']/div/div[1]/h2")
	TITLE_GRID_5 = (By.XPATH, "//*[@id='desktop-grid-5']/div/div[1]/h2")
	TITLE_GRID_6 = (By.XPATH, "//*[@id='desktop-grid-6']/div/div[1]/h2")
	TITLE_GRID_7 = (By.XPATH, "//*[@id='desktop-grid-7']/div/div[1]/h2")
	# Category titles after clicking hrefs at the top of the page
	TITLE_AMAZONBASIC = (By.XPATH, "//*[@id='search']/span/div/span/h1/div/div[1]/div/div/span[3]")
	TITLE_SHOP_BY_CAT = (By.XPATH, "//*[@id='a-page']/div[2]/div[2]/div[1]/div[1]/div/h1")
	TITLE_ELECTRONICS = (By.XPATH, "//*[@id='a-page']/div[2]/div[2]/div[1]/div[1]/div/h1")
	TITLE_COMPUTERS_ACCESSORIES  = (By.XPATH, "//*[@id='a-page']/div[2]/div[2]/div[1]/div[1]/div/h1")
	TITLE_SHOP_TOP  = (By.CSS_SELECTOR, "img[alt='Shop top categories']")
	TITLE_BEUATY_PICKS = (By.XPATH, "//*[@id='a-page']/div[2]/div[2]/div[1]/div[1]/div/h1")
	TITLE_GET_FIT = (By.XPATH, "//*[@id='a-page']/div[2]/div[2]/div[1]/div[1]/div/h1")
	TITLE_DEALS_PROM = (By.XPATH, "//*[@id='a-page']/div[2]/div[2]/div[1]/div[1]/div/h1")
	TITLE_EASY_RETURNS = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div/div[3]/h1")
	TITLE_SHIPS_WORLDWIDE = (By.XPATH, "//*[@id='a-page']/div[2]/div/div/div/div/div/div/div/div[3]/div[1]/div[2]/div/h1")
	TITLE_IDEAL_TV = (By.XPATH, "//*[@id='departments']/ul/li[2]/span/a/span[2]")
	# Category titles after clicking hrefs at the middle of the page
	TITLE_COMFY_STYLES = (By.XPATH, "//*[@id='a-page']/div[2]/div[2]/div[1]/div[1]/div/h1")
	TITLE_LAPTOP_TABLETS = (By.XPATH, "//*[@id='departments']/ul/li[2]/span/span")
	TITLE_HOME_BEDDING = (By.XPATH, "//*[@id='search']/span/div/span/h1/div/div[1]/div/div/span[3]")
	TITLE_STRIP_LIGHTS = (By.XPATH, "//*[@id='search']/span/div/span/h1/div/div[1]/div/div/span[3]")

	BACK_TO_TOP = (By.ID, "navBackToTop") # Button at the bottom
	LOGO_BOTTOM = (By.XPATH, "//*[@id='navFooter']/div[3]/span[1]/div/a/div")
	LANG_CHANGE = (By.CSS_SELECTOR, "img[alt='Shop in 8 different languages']")


class LangPageLocators:
	ENGLISH_CHECK = (By.XPATH, "//*[@id='customer-preferences']/div/div/form/div[1]/div[1]/div[1]/div/label")
	ESPANOL_CHECK = (By.XPATH, "//*[@id='customer-preferences']/div/div/form/div[1]/div[1]/div[2]/div/label")
	DEUTSCH_CHECK = (By.XPATH, "//*[@id='customer-preferences']/div/div/form/div[1]/div[1]/div[4]/div/label")
	PORTUGUES_CHECK = (By.XPATH, "//*[@id='customer-preferences']/div/div/form/div[1]/div[1]/div[5]/div/label")
	TEXT_BOX = (By.ID, "icp-sl-t-text") # Text box on the right

	CURRENCY_SET = (By.ID, "a-autoid-0-announce")
	CURRENCY_TEXT = (By.ID, "icp-sc-note") # Text box on the bottom
	USD = (By.ID, "icp-sc-dropdown_1")
	ARS = (By.ID, "icp-sc-dropdown_3")
	EURO = (By.ID, "icp-sc-dropdown_23")
	HONG_KONG = (By.ID, "icp-sc-dropdown_27")
	NOK = (By.ID, "icp-sc-dropdown_46")
	POUNDS = (By.ID, "icp-sc-dropdown_51")
	VND = (By.ID, "icp-sc-dropdown_64")
	CANCEL_BUTTON = (By.ID, "icp-btn-close-announce")


class RegisterPageLocators:
	DROP_MENU = (By.ID, "nav-link-accountList") # Navbar on the home page
	SIGN_UP = (By.XPATH, "//*[@id='nav-flyout-ya-newCust']/a")
	CREATE_ACC_BUTTON = (By.ID, "continue")

	NAME_ALERT = (By.XPATH, "//*[@id='auth-customerName-missing-alert']/div/div")
	EMAIL_ALERT = (By.XPATH, "//*[@id='auth-email-missing-alert']/div/div")
	INVALID_EMAIL_ALERT = (By.XPATH, "//*[@id='auth-email-invalid-email-alert']/div/div")
	PASSWORD_ALERT = (By.XPATH, "//*[@id='auth-password-missing-alert']/div/div")
	SHORT_PASSWORD_ALERT = (By.XPATH, "//*[@id='auth-password-invalid-password-alert']/div/div")		
	RE_PASSWORD_ALERT = (By.XPATH, "//*[@id='auth-passwordCheck-missing-alert']/div/div")
	MISMATCH_PASSWORD_ALERT = (By.XPATH, "//*[@id='auth-password-mismatch-alert']/div/div")

	NAME_INPUT = (By.ID, "ap_customer_name")
	EMAIL_INPUT = (By.ID, "ap_email")
	PASSWORD_INPUT = (By.ID, "ap_password")
	RE_PASSWORD_INPUT = (By.ID, "ap_password_check")

	BOX_PROBLEM_ALERT = (By.XPATH, "//*[@id='auth-error-message-box']/div/h4")
	# Placeholders are empty ; fill invalid email ; fill one password placeholder or different passwords
	BOX_NAME_ALERT_0 = (By.XPATH, "//*[@id='auth-error-message-box']/div/div/dl/li[1]/span")
	BOX_EMAIL_ALERT_0 = (By.XPATH, "//*[@id='auth-error-message-box']/div/div/dl/li[2]/span")
	BOX_PASSWORD_ALERT_0 = (By.XPATH, "//*[@id='auth-error-message-box']/div/div/dl/li[3]/span")
	# Name placeholder is fill
	BOX_EMAIL_ALERT_1 = (By.XPATH, "//*[@id='auth-error-message-box']/div/div/dl/li[1]/span")
	BOX_PASSWORD_ALERT_1 = (By.XPATH, "//*[@id='auth-error-message-box']/div/div/dl/li[2]/span")


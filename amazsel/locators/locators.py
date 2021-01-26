from selenium.webdriver.common.by import By

class MainPageLocators:
	LOGO_URL = 'https://www.amazon.com/ref=nav_logo'
	LOGO = (By.ID, "nav-logo-sprites")
	DESKTOP_GRID_1 = (By.XPATH, "//*[@id='desktop-grid-1']/div/div[3]/a")
	DESKTOP_GRID_2 = (By.XPATH, "//*[@id='desktop-grid-2']/div/div[3]/a")
	DESKTOP_GRID_3 = (By.XPATH, "//*[@id='desktop-grid-3']/div/div[3]/a")
	DESKTOP_GRID_4 = (By.XPATH, "//*[@id='desktop-grid-4']/div/div[3]/a")
	DESKTOP_GRID_5 = (By.XPATH, "//*[@id='desktop-grid-5']/div/div[3]/a")
	DESKTOP_GRID_6 = (By.XPATH, "//*[@id='desktop-grid-6']/div/div[3]/a")
	DESKTOP_GRID_7 = (By.XPATH, "//*[@id='desktop-grid-7']/div/div[3]/a")
	DESKTOP_GRID_1_D2 = (By.CSS_SELECTOR, "img[alt='We ship 45 million products around the world']")
	DESKTOP_BTF_GRID_1 = (By.XPATH, "//*[@id='desktop-btf-grid-1']/div/div[3]/a")
	DESKTOP_BTF_GRID_2 = (By.XPATH, "//*[@id='desktop-btf-grid-2']/div/div[3]/a")
	DESKTOP_BTF_GRID_3 = (By.XPATH, "//*[@id='desktop-btf-grid-3']/div/div[3]/a")
	DESKTOP_BTF_GRID_4 = (By.XPATH, "//*[@id='desktop-btf-grid-4']/div/div[3]/a")

	TITLE_GRID_1 = (By.XPATH, "//*[@id='desktop-grid-1']/div/div[1]/h2")
	TITLE_GRID_2 = (By.XPATH, "//*[@id='desktop-grid-2']/div/div[1]/h2")
	TITLE_GRID_3 = (By.XPATH, "//*[@id='desktop-grid-3']/div/div[1]/h2")
	TITLE_GRID_4 = (By.XPATH, "//*[@id='desktop-grid-4']/div/div[1]/h2")
	TITLE_GRID_5 = (By.XPATH, "//*[@id='desktop-grid-5']/div/div[1]/h2")
	TITLE_GRID_6 = (By.XPATH, "//*[@id='desktop-grid-6']/div/div[1]/h2")
	TITLE_GRID_7 = (By.XPATH, "//*[@id='desktop-grid-7']/div/div[1]/h2")

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

	TITLE_COMFY_STYLES = (By.XPATH, "//*[@id='a-page']/div[2]/div[2]/div[1]/div[1]/div/h1")
	TITLE_LAPTOP_TABLETS = (By.XPATH, "//*[@id='departments']/ul/li[2]/span/span")
	TITLE_HOME_BEDDING = (By.XPATH, "//*[@id='search']/span/div/span/h1/div/div[1]/div/div/span[3]")
	TITLE_STRIP_LIGHTS = (By.XPATH, "//*[@id='search']/span/div/span/h1/div/div[1]/div/div/span[3]")

	BACK_TO_TOP = (By.ID, "navBackToTop")
	LOGO_BOTTOM = (By.XPATH, "//*[@id='navFooter']/div[3]/span[1]/div/a/div")



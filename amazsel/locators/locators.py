from selenium.webdriver.common.by import By

class MainPageLocators:
	LOGO_URL = 'https://www.amazon.com/ref=nav_logo'
	LOGO = [By.ID, 'nav-logo-sprites']
	DESKTOP_GRID_1 = (By.XPATH, '//*[@id="desktop-grid-1"]/div/div[3]/a')
	DESKTOP_GRID_2 = (By.XPATH, '//*[@id="desktop-grid-2"]/div/div[3]/a')
	DESKTOP_GRID_3 = (By.XPATH, '//*[@id="desktop-grid-3"]/div/div[3]/a')
	DESKTOP_GRID_4 = (By.XPATH, '//*[@id="desktop-grid-4"]/div/div[3]/a')
	DESKTOP_GRID_5 = (By.XPATH, '//*[@id="desktop-grid-5"]/div/div[3]/a')
	DESKTOP_GRID_6 = (By.XPATH, '//*[@id="desktop-grid-6"]/div/div[3]/a')
	DESKTOP_GRID_7 = (By.XPATH, '//*[@id="desktop-grid-7"]/div/div[3]/a')
	DESKTOP_GRID_8 = (By.XPATH, '//*[@id="gw-card-layout"]/div[9]/div[1]/div[3]/a')



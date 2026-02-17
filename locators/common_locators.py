from selenium.webdriver.common.by import By

#======================Локаторы header======================
HEADER_YANDEX_LOGO = (By.CSS_SELECTOR, "img[alt='Yandex']")
HEADER_SCOOTER_LOGO = (By.CSS_SELECTOR, "img[alt='Scooter']")
#======================Локаторы банера cookie======================
COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")
COOKIE_BANNER = (By.CSS_SELECTOR, "div.App_CookieConsent__1yUIN")
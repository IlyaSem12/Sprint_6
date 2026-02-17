#./pages/base_page.py
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from config import *


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url: str):
        '''Метод открытия страницы'''
        self.browser.get(url)

    def wait_visible(self, locator, timeout: int = 10):
        '''Метод ожидания появления элемента'''
        return WebDriverWait(self.browser, timeout).until(expected_conditions.visibility_of_element_located(locator))
    
    def wait_invisible(self, locator, timeout: int = 10):
        '''Метод ожидает что элемент исчез'''
        return WebDriverWait(self.browser, timeout).until(expected_conditions.invisibility_of_element_located(locator))

    def is_visible(self, locator, timeout=5):
        '''Метод проверяет, что элемент появился'''
        try:
            self.wait_visible(locator, timeout)
            return True
        except TimeoutException:
            return False
    
    def click(self, locator, timeout: int = 10):
        '''Метод для нажатия по элементу'''
        element = WebDriverWait(self.browser, timeout).until(expected_conditions.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.browser.execute_script("arguments[0].click();", element)
    
    def scroll_to_element(self, locator, timeout: int = 10):
        """Метод скроллит страницу до элемента."""
        element = self.wait_visible(locator, timeout)
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});",element)
        return element
    
    def get_text(self,locator, timeout: int = 10):
        '''Метод полчения текста элемента '''
        return self.wait_visible(locator, timeout).text.strip()
    
    def send_text(self, locator, text, timeout: int = 10):
        '''Метод вставки текста в поле ввода'''
        self.wait_visible(locator, timeout).send_keys(text)
    
    def get_current_url(self):
        '''Метод для получения текучшего url'''
        return self.browser.current_url
    
    def wait_switch_to_window(self, url:str, timeout: int = 10):
        '''Метод для переключения вкладки и ожидания ее загрузки'''
        self.browser.switch_to.window(self.browser.window_handles[-1]) # переключаемся на последнюю вкладку
        WebDriverWait(self.browser, timeout).until(expected_conditions.url_to_be(url))  # ждём загрузки страницы

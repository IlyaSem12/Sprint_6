import pytest
import allure
from config import *
from selenium import webdriver 
from pages.main_page import MainPageScooter
from locators.main_page_locators import *
from locators.common_locators import *
from locators.order_page_locators import *
from helpers import *


@pytest.fixture
def browser():
    '''Фикструа для получения инстанса драйвера'''
    with allure.step("Окрываем браузер"):
        driver = webdriver.Firefox()
        driver.maximize_window()
    yield driver
    with allure.step("Закрываем браузер"):
        driver.quit()

@pytest.fixture()
def main_page(browser):
    """Фикстура для перехода на главную страницу"""
    with allure.step(f"Преходим на главную страницу '{BASE_URL}'"):
        page = MainPageScooter(browser)#Создаем объект класса MainPageScooter
        page.open(BASE_URL) #переходим по ссылке
        #добавляем явное ожиданяие для прогрузки страницы
        page.wait_for_load_main_page()
        page.accept_cookies() #Принимаем куки
    return page


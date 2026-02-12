import allure
import pytest
from conftest import *
from config import *


@allure.epic("Главная страница")
@allure.tag('main page')
@pytest.mark.gui
class TestMainPage:
    
    @allure.feature("FAQ dropdown menu")
    @allure.title('Проверка выпадающего списка "Сколько это стоит? И как оплатить?"')
    def test_main_page_click_faq_payment_shows_correct_text(self,main_page):
        '''Тест проверяет корректность работы dropdown menu FAQ: стоимость и оплата.'''
        page = main_page
        page.wait_for_load_faq_card()
        description = page.get_faq_answer_by_text(QUESTION_PRICE_AND_PAYMENT_DROPDOWN_MENU,ANSWER_PRICE_AND_PAYMENT_DROPDOWN_MENU)
        assert description == FAQ_PRICE_AND_PAYMENT_TEXT, f'Описание не сопадают!\nОжидалось:"{FAQ_PRICE_AND_PAYMENT_TEXT}";\nПолучили:"{description}"'
    
    @allure.feature("FAQ dropdown menu")
    @allure.title('Проверка выпадающего списка "Хочу сразу несколько самокатов! Так можно?"')
    def test_main_page_click_faq_multiple_scooters_shows_correct_text(self,main_page):
        '''Тест проверяет корректность работы dropdown menu FAQ: Несколько самокатов.'''
        page = main_page
        page.wait_for_load_faq_card()
        description = page.get_faq_answer_by_text(QUESTION_MULTIPLE_SCOOTERS_DROPDOWN_MENU,ANSWER_MULTIPLE_SCOOTERS_DROPDOWN_MENU)
        assert description == FAQ_MULTIPLE_SCOOTERS_TEXT, f'Описание не сопадают!\nОжидалось:"{FAQ_MULTIPLE_SCOOTERS_TEXT}";\nПолучили:"{description}"'
    
    @allure.feature("FAQ dropdown menu")
    @allure.title('Проверка выпадающего списка "Как рассчитывается время аренды?"')
    def test_main_page_click_faq_rent_time_calculations_shows_correct_text(self,main_page):
        '''Тест проверяет корректность работы dropdown menu FAQ: Расчёт времени аренды.'''
        page = main_page
        page.wait_for_load_faq_card()
        description = page.get_faq_answer_by_text(QUESTION_RENT_TIME_CALCULATION_DROPDOWN_MENU,ANSWER_RENT_TIME_CALCULATION_DROPDOWN_MENU)
        assert description == FAQ_RENT_TIME_CALCULATION_TEXT, f'Описание не сопадают!\nОжидалось:"{FAQ_RENT_TIME_CALCULATION_TEXT}";\nПолучили:"{description}"'
    
    @allure.feature("FAQ dropdown menu")
    @allure.title('Проверка выпадающего списка "Можно ли заказать самокат прямо на сегодня?"')
    def test_main_page_click_faq_order_today_shows_correct_text(self,main_page):
        '''Тест проверяет корректность работы dropdown menu FAQ: Заказ на сегодня.'''
        page = main_page
        page.wait_for_load_faq_card()
        description = page.get_faq_answer_by_text(QUESTION_ORDER_FOR_TODAY_DROPDOWN_MENU,ANSWER_ORDER_FOR_TODAY_DROPDOWN_MENU)
        assert description == FAQ_ORDER_TODAY_TEXT, f'Описание не сопадают!\nОжидалось:"{FAQ_ORDER_TODAY_TEXT}";\nПолучили:"{description}"'
    
    @allure.feature("FAQ dropdown menu")
    @allure.title('Проверка выпадающего списка "Можно ли продлить заказ или вернуть самокат раньше?"')
    def test_main_page_click_faq_extend_or_return_shows_correct_text(self,main_page):
        '''Тест проверяет корректность работы dropdown menu FAQ: Продление или ранний возврат.'''
        page = main_page
        page.wait_for_load_faq_card()
        description = page.get_faq_answer_by_text(QUESTION_EXTEND_OR_RETURN_DROPDOWN_MENU,ANSWER_EXTEND_OR_RETURN_DROPDOWN_MENU)
        assert description == FAQ_EXTEND_OR_RETURN_TEXT, f'Описание не сопадают!\nОжидалось:"{FAQ_EXTEND_OR_RETURN_TEXT}";\nПолучили:"{description}"'

    @allure.feature("FAQ dropdown menu")
    @allure.title('Проверка выпадающего списка "Можно ли отменить заказ?"')
    def test_main_page_click_faq_order_cansellation_shows_correct_text(self,main_page):
        '''Тест проверяет корректность работы dropdown menu FAQ: Отмена заказа'''
        page = main_page
        page.wait_for_load_faq_card()
        description = page.get_faq_answer_by_text(QUESTION_ORDER_CANCELLATION_DROPDOWN_MENU,ANSWER_ORDER_CANCELLATION_DROPDOWN_MENU)
        assert description == FAQ_ORDER_CANCELLATION_TEXT , f'Описание не сопадают!\nОжидалось:"{FAQ_ORDER_CANCELLATION_TEXT }";\nПолучили:"{description}"'
    
    @allure.feature("FAQ dropdown menu")
    @allure.title('Проверка выпадающего списка "Я жизу за МКАДом, привезёте?"')
    def test_main_page_click_faq_delivery_outside_mkad_shows_correct_text(self,main_page):
        '''Тест проверяет корректность работы dropdown menu FAQ: Доставка за МКАД'''
        page = main_page
        page.wait_for_load_faq_card()
        description = page.get_faq_answer_by_text(QUESTION_DELIVERY_OUTSIDE_MKAD_DROPDOWN_MENU,ANSWER_DELIVERY_OUTSIDE_MKAD_DROPDOWN_MENU)
        assert description == FAQ_DELIVERY_OUTSIDE_MKAD_TEXT , f'Описание не сопадают!\nОжидалось:"{FAQ_DELIVERY_OUTSIDE_MKAD_TEXT }";\nПолучили:"{description}"'
    
    
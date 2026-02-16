import allure
import pytest
from conftest import *
from config import *


@allure.epic("Главная страница")
@allure.tag('main page')
@pytest.mark.gui
class TestMainPage:
    
    @allure.feature("FAQ dropdown menu")
    @pytest.mark.parametrize(
    "question_dropdown_menu, answer_dropdown_menu, faq_text",
    [
        (QUESTION_PRICE_AND_PAYMENT_DROPDOWN_MENU, ANSWER_PRICE_AND_PAYMENT_DROPDOWN_MENU, FAQ_PRICE_AND_PAYMENT_TEXT),
        (QUESTION_MULTIPLE_SCOOTERS_DROPDOWN_MENU, ANSWER_MULTIPLE_SCOOTERS_DROPDOWN_MENU, FAQ_MULTIPLE_SCOOTERS_TEXT),
        (QUESTION_RENT_TIME_CALCULATION_DROPDOWN_MENU, ANSWER_RENT_TIME_CALCULATION_DROPDOWN_MENU, FAQ_RENT_TIME_CALCULATION_TEXT),
        (QUESTION_ORDER_FOR_TODAY_DROPDOWN_MENU, ANSWER_ORDER_FOR_TODAY_DROPDOWN_MENU, FAQ_ORDER_TODAY_TEXT),
        (QUESTION_EXTEND_OR_RETURN_DROPDOWN_MENU, ANSWER_EXTEND_OR_RETURN_DROPDOWN_MENU, FAQ_EXTEND_OR_RETURN_TEXT),
        (QUESTION_ORDER_CANCELLATION_DROPDOWN_MENU, ANSWER_ORDER_CANCELLATION_DROPDOWN_MENU, FAQ_ORDER_CANCELLATION_TEXT),
        (QUESTION_DELIVERY_OUTSIDE_MKAD_DROPDOWN_MENU, ANSWER_DELIVERY_OUTSIDE_MKAD_DROPDOWN_MENU, FAQ_DELIVERY_OUTSIDE_MKAD_TEXT),
    ], ids=[
        "faq_price_and_payment",
        "faq_multiply_scooters",
        "faq_rent_time_calculation",
        "faq_order_for_today",
        "faq_exyend_or_return",
        "faq_order_cancellation",
        "faq_deleivery_outside_mkad",
    ])
    def test_main_page_click_faq_dropdown_menu_shows_correct_text(self,main_page, question_dropdown_menu, answer_dropdown_menu, faq_text):
        '''Тест проверяет корректность работы dropdown menu FAQ'''
        page = main_page
        page.wait_for_load_faq_card()
        allure.dynamic.title(f'Проверка выпадающего списка "{page.get_faq_question_by_text(question_dropdown_menu)}"')
        description = page.get_faq_answer_by_text(question_dropdown_menu,answer_dropdown_menu)
        with allure.step("Сравниваем описания текста"):
            assert description == faq_text, f'Описание не сопадают!\nОжидалось:"{faq_text}";\nПолучили:"{description}"'
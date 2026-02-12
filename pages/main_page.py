#./pages/main_page.py
import allure
from locators.main_page_locators import *
from locators.common_locators import *
from pages.base_page import BasePage
from pages.order_page import OrderPageScooter
from config import *


class MainPageScooter(BasePage):
    
    @allure.step('Ожидаем загрузку страницы по появлению поля Яндекс')
    def wait_for_load_main_page(self):
        self.wait_visible(HEADER_YANDEX_LOGO, 5)
    
    @allure.step('Ожидаем загрузку блока "Вопросы о важном"')
    def wait_for_load_faq_card(self):
        self.wait_visible(FAQ_CARD, 5)
    
    @allure.step('Скроллим до карточки FAQ')
    def scroll_faq_card(self):
        self.scroll_to_element(FAQ_CARD)

    @allure.step('Подтверждаем куки')
    def accept_cookies(self):
        self.click(COOKIE_ACCEPT_BUTTON)
        self.wait_invisible(COOKIE_BANNER)
    
    @allure.step('Нажимаем на лого "Яндекс"')
    def click_header_yandex(self):
        self.click(HEADER_YANDEX_LOGO)

    @allure.step('Нажимаем на пункт с вопросом карточки FAQ')
    def click_faq_question_menu(self, question_locator):
        self.scroll_faq_card()
        self.click(question_locator)

    @allure.step('Получаем текст ответа в FAQ')
    def get_faq_answer_by_text(self, question_locator, answer_locator):
        self.click_faq_question_menu(question_locator)
        return self.get_text(answer_locator)

    @allure.step('Нажимаем на верхнюю кнопку "Звказать"')
    def click_order_button_top(self):
        self.click(ORDER_BUTTON_TOP)
        return OrderPageScooter(self.browser)
    
    allure.step('Нажимаем на нижнюю кнопку "Звказать"')
    def click_order_button_bottom(self):
        self.click(ORDER_BUTTON_BOTTOM)
        return OrderPageScooter(self.browser)
    
    allure.step(f'Ожидаем пепрехода на {DZEN_URL}')
    def wait_for_switch_to_dzen_page(self):
        self.wait_switch_to_window(DZEN_URL)
    

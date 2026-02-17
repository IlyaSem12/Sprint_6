#./pages/order_page.py
import allure
from locators.main_page_locators import *
from locators.common_locators import *
from locators.order_page_locators import *
from pages.base_page import BasePage
from config import *
from selenium.webdriver.common.keys import Keys
from helpers import *


class OrderPageScooter(BasePage):
    
    @allure.step('Ожидаем загрузку страницы по появлению поля Яндекс')
    def wait_for_load_order_page(self):
        self.wait_visible(HEADER_YANDEX_LOGO, 5)
    
    @allure.step('Ожидаем загрузку блока "Для кого самокат"')
    def wait_for_load_order_form_card(self):
        self.wait_visible(ORDER_FORM_CARD, 5)
    
    @allure.step('Нажимаем кнопку "Далее"')
    def click_button_next(self):
        self.click(NEXT_BUTTON)
    
    @allure.step('Нажимаем кнопку "Заказать"')
    def click_button_order(self):
        self.click(ORDER_BUTTON)
    
    @allure.step('Нажимаем кнопку "Заказать"')
    def click_button_order(self):
        self.click(ORDER_BUTTON)
    
    @allure.step('Нажимаем кнопку подтверждения заказа')
    def click_button_confirm(self):
        self.click(CONFIRM_YES_BUTTON)
    
    @allure.step('Нажимаем кнопку подтверждения заказа')
    def click_button_view_status(self):
        self.click(VIEW_STATUS_BUTTON)
    
    @allure.step('Нажимаем на лого "Самокат"')
    def click_header_scooter(self):
        self.click(HEADER_SCOOTER_LOGO)

    @allure.step('Ожидаем загрузку окна с подверждением заказа')
    def wait_for_load_confirm_modal(self):
        self.wait_visible(CONFIRM_MODAL)
    
    def set_rent_period_input(self, rent_period):
        self.click(RENT_PERIOD_DROPDOWN)
        self.click(rent_period)

    def set_metro_input(self,name_metro:str):
        self.click(INPUT_METRO)
        self.send_text(INPUT_METRO, name_metro)
        self.send_text(INPUT_METRO, Keys.ARROW_DOWN)
        self.send_text(INPUT_METRO, Keys.ENTER)
    
    def set_delivery_date_input(self):
        delivery_date = get_next_day()
        self.send_text(DELIVERY_DATE_INPUT, delivery_date)
        self.send_text(DELIVERY_DATE_INPUT, Keys.ENTER)

    @allure.step('Заполняем данные заказчика')
    def fill_customer_data(self, data:dict):
        phone = generate_phone()
        self.wait_for_load_order_form_card()
        self.send_text(INPUT_NAME, data['first_name'])
        self.send_text(INPUT_LASTNAME, data['last_name'])
        self.send_text(INPUT_ADDRESS, data['address'])
        self.set_metro_input(data['metro'])
        self.send_text(INPUT_PHONE, phone)
        self.click_button_next()
    
    @allure.step('Заполняем данные аренды самоката')
    def fill_rent_data(self, data:dict):
        self.wait_for_load_order_form_card()
        self.set_delivery_date_input()
        self.set_rent_period_input(data['rent_period'])
        self.click(data['color'])
        self.send_text(COURIER_COMMENT_INPUT,data['comment'] )
        self.click_button_order()

    
        
import allure
import pytest
from conftest import *
from config import *

@allure.epic("Cтраница заказа")
@allure.tag('order page')
@pytest.mark.gui
class TestOrderPage:
    
    @allure.feature("Order form")
    @allure.title('Проверка формы заказа"')
    @pytest.mark.parametrize(
    "click_method, order_data",
    [
        ("click_order_button_top", TEST_ORDER_DATA[0]),
        ("click_order_button_bottom", TEST_ORDER_DATA[1]),
    ], ids=[
        "TopButton_BlackScooter",
        "BottomButton_GreyScooter",
    ])
    def test_order_page_success_fill_rent_data_shows_track_page_redirect_urls(self,main_page, click_method, order_data):
        '''Тест проверяет корректность работы страницы заказа, редирект на главную странцу при нажатии на лого "Самокат" и открытие странички Дзен при нажатии на лого "Яндекс".'''
        base_page = main_page
        order_page = getattr(base_page, click_method)()
        order_page.fill_customer_data(order_data)
        order_page.fill_rent_data(order_data)
        order_page.wait_for_load_confirm_modal()
        order_page.click_button_confirm()
        assert order_page.is_visible(SUCCESS_MODAL_TITLE, 5), "Всплывающее окно с успешным созданием заказа не появилось"
        order_page.click_button_view_status()
        order_page.click_header_scooter()
        assert order_page.get_current_url() == BASE_URL, f'Редирект на "{BASE_URL}" не был осуществлен'
        base_page.click_header_yandex()
        base_page.wait_for_switch_to_dzen_page()
        assert DZEN_URL == base_page.get_current_url(), f'Страница "{DZEN_URL}" не открылась'
        

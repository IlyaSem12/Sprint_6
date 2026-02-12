from locators.order_page_locators import *
#================CONSTANT URLS================
BASE_URL = 'https://qa-scooter.praktikum-services.ru/'
ORDER_URL = f'{BASE_URL}order'
DZEN_URL = 'https://dzen.ru/?yredirect=true'
#================CONSTANT DATA================
FAQ_PRICE_AND_PAYMENT_TEXT = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
FAQ_MULTIPLE_SCOOTERS_TEXT = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
FAQ_RENT_TIME_CALCULATION_TEXT = (
    "Допустим, вы оформляете заказ на 8 мая. "
    "Мы привозим самокат 8 мая в течение дня. "
    "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. "
    "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
)
FAQ_ORDER_TODAY_TEXT = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
FAQ_EXTEND_OR_RETURN_TEXT = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
FAQ_CHARGER_INCLUDED_TEXT = (
    "Самокат приезжает к вам с полной зарядкой. "
    "Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. "
    "Зарядка не понадобится."
)
FAQ_ORDER_CANCELLATION_TEXT = (
    "Да, пока самокат не привезли. "
    "Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
)
FAQ_DELIVERY_OUTSIDE_MKAD_TEXT = "Да, обязательно. Всем самокатов! И Москве, и Московской области."

TEST_ORDER_DATA = [
    {
        "first_name": "Илья",
        "last_name": "Смирнов",
        "address": "г. Москва, ул. Ленина, д. 10",
        "metro": "Черкизовская",
        "phone": "+78005553535",
        "rent_period": RENT_PERIOD_TWO_DAYS,
        "color": COLOR_BLACK_CHECKBOX,
        "comment": "Позвонить за 10 минут"
    },
    {
        "first_name": "Анна",
        "last_name": "Кузнецова",
        "address": "г. Москва, ул. Тверская, д. 15",
        "metro": "Сокольники",
        "phone": "+79997654321",
        "rent_period": RENT_PERIOD_ONE_DAY,
        "color": COLOR_GREY_CHECKBOX,
        "comment": "Домофон не работает"
    }
]
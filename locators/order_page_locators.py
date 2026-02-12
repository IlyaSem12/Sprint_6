from selenium.webdriver.common.by import By


#======================Локаторы полей ввода для оформления заказа======================
#Локатор для карты со всеми полями ввода
ORDER_FORM_CARD = (By.CSS_SELECTOR, "div.Order_Form__17u6u")
#Поле ввода имени
INPUT_NAME = (By.XPATH,"//input[@placeholder='* Имя']")
#Поле ввода фамилии
INPUT_LASTNAME = (By.XPATH,"//input[@placeholder='* Фамилия']")
#Поле ввода адреса заказа
INPUT_ADDRESS = (By.XPATH,"//input[@placeholder='* Адрес: куда привезти заказ']")
#Поле ввода станции метро
INPUT_METRO = (By.XPATH,"//input[@placeholder='* Станция метро']")
#Поле ввода номера телефона
INPUT_PHONE = (By.XPATH,"//input[@placeholder='* Телефон: на него позвонит курьер']")
NEXT_BUTTON = (By.XPATH,"//button[normalize-space()='Далее']")
# Дата доставки (поле ввода)
DELIVERY_DATE_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
# Срок аренды 
RENT_PERIOD_DROPDOWN = (By.CSS_SELECTOR, ".Dropdown-control[aria-haspopup='listbox']")
RENT_PERIOD_ONE_DAY = (By.XPATH,"//div[@role='option' and normalize-space()='сутки']")
RENT_PERIOD_TWO_DAYS = (By.XPATH,"//div[@role='option' and normalize-space()='двое суток']")
# Цвета (чекбоксы) — тут идеально, потому что есть id
COLOR_BLACK_CHECKBOX = (By.ID, "black")
COLOR_GREY_CHECKBOX = (By.ID, "grey")
# Комментарий для курьера
COURIER_COMMENT_INPUT = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")
ORDER_BUTTON =(By.XPATH, "//div[contains(@class, 'Order_Content')]//button[text()='Заказать']")
#======================Локаторы полей подтверждения заказа======================
# Карточка/контейнер модального окна
CONFIRM_MODAL = (By.XPATH, "//div[contains(@class,'Order_Modal')]")
# Заголовок модалки (текст "Хотите оформить заказ?")
CONFIRM_MODAL_TITLE = (By.XPATH,"//div[contains(@class,'Order_Modal')]//div[contains(@class,'Order_ModalHeader') and contains(normalize-space(), 'Хотите оформить заказ?')]")
# Кнопка "Да" внутри модалки
CONFIRM_YES_BUTTON = (
    By.XPATH,
    "//div[contains(@class,'Order_Modal')]//div[contains(@class,'Order_Buttons')]//button[normalize-space()='Да']"
)
#======================Локаторы полей “Заказ оформлен”======================
# Карточка модального окна
SUCCESS_MODAL = (By.XPATH,"//div[contains(@class,'Order_Modal')]")
# Заголовок "Заказ оформлен"
SUCCESS_MODAL_TITLE = (By.XPATH,"//div[contains(@class,'Order_Modal')]//div[contains(@class,'Order_ModalHeader') and contains(normalize-space(),'Заказ оформлен')]")
# Текст с номером заказа
ORDER_NUMBER_TEXT = (By.XPATH,"//div[contains(@class,'Order_Modal')]//div[contains(@class,'Order_Text') and contains(text(),'Номер заказа')]")
# Кнопка "Посмотреть статус"
VIEW_STATUS_BUTTON = (By.XPATH,"//div[contains(@class,'Order_Modal')]//button[normalize-space()='Посмотреть статус']")

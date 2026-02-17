from selenium.webdriver.common.by import By

#======================Локаторы Конопок заказать======================
# Верхняя кнопка "Заказать"
ORDER_BUTTON_TOP = (By.XPATH,"(//button[normalize-space()='Заказать'])[1]")
# нижняякнопка "Заказать"
ORDER_BUTTON_BOTTOM = (By.XPATH,"(//button[normalize-space()='Заказать'])[2]")
#======================Локаторы Dropdown menu======================
#Локатор для карты со всеми вопросами
FAQ_CARD = (By.XPATH, "//div[@data-accordion-component='AccordionItem']")
#  1) Стоимость и оплата
QUESTION_PRICE_AND_PAYMENT_DROPDOWN_MENU = (By.CSS_SELECTOR,"div.Home_FAQ__3uVm4 #accordion__heading-0[data-accordion-component='AccordionItemButton']")
ANSWER_PRICE_AND_PAYMENT_DROPDOWN_MENU = (By.CSS_SELECTOR,"div.Home_FAQ__3uVm4 #accordion__panel-0[data-accordion-component='AccordionItemPanel'] p")
# 2) Несколько самокатов
QUESTION_MULTIPLE_SCOOTERS_DROPDOWN_MENU = (By.CSS_SELECTOR,"div.Home_FAQ__3uVm4 #accordion__heading-1[data-accordion-component='AccordionItemButton']")
ANSWER_MULTIPLE_SCOOTERS_DROPDOWN_MENU = (By.CSS_SELECTOR,"div.Home_FAQ__3uVm4 #accordion__panel-1[data-accordion-component='AccordionItemPanel'] p")
# 3) Расчёт времени аренды
QUESTION_RENT_TIME_CALCULATION_DROPDOWN_MENU = (By.CSS_SELECTOR,"div.Home_FAQ__3uVm4 #accordion__heading-2[data-accordion-component='AccordionItemButton']")
ANSWER_RENT_TIME_CALCULATION_DROPDOWN_MENU = (By.CSS_SELECTOR,"div.Home_FAQ__3uVm4 #accordion__panel-2[data-accordion-component='AccordionItemPanel'] p")
# 4) Заказ на сегодня
QUESTION_ORDER_FOR_TODAY_DROPDOWN_MENU = (By.CSS_SELECTOR,"div.Home_FAQ__3uVm4 #accordion__heading-3[data-accordion-component='AccordionItemButton']")
ANSWER_ORDER_FOR_TODAY_DROPDOWN_MENU = (By.CSS_SELECTOR,"div.Home_FAQ__3uVm4 #accordion__panel-3[data-accordion-component='AccordionItemPanel'] p")
# 5) Продление или ранний возврат
QUESTION_EXTEND_OR_RETURN_DROPDOWN_MENU = (By.CSS_SELECTOR,"div.Home_FAQ__3uVm4 #accordion__heading-4[data-accordion-component='AccordionItemButton']")
ANSWER_EXTEND_OR_RETURN_DROPDOWN_MENU = (By.CSS_SELECTOR,"div.Home_FAQ__3uVm4 #accordion__panel-4[data-accordion-component='AccordionItemPanel'] p")
# 6) Зарядка в комплекте
QUESTION_CHARGER_INCLUDED_DROPDOWN_MENU = (By.CSS_SELECTOR,"div.Home_FAQ__3uVm4 #accordion__heading-5[data-accordion-component='AccordionItemButton']")
ANSWER_CHARGER_INCLUDED_DROPDOWN_MENU = (By.CSS_SELECTOR,"div.Home_FAQ__3uVm4 #accordion__panel-5[data-accordion-component='AccordionItemPanel'] p")
# 7) Отмена заказа
QUESTION_ORDER_CANCELLATION_DROPDOWN_MENU = (By.CSS_SELECTOR,"div.Home_FAQ__3uVm4 #accordion__heading-6[data-accordion-component='AccordionItemButton']"
)
ANSWER_ORDER_CANCELLATION_DROPDOWN_MENU = (By.CSS_SELECTOR,"div.Home_FAQ__3uVm4 #accordion__panel-6[data-accordion-component='AccordionItemPanel'] p")
# 8) Доставка за МКАД
QUESTION_DELIVERY_OUTSIDE_MKAD_DROPDOWN_MENU = (By.CSS_SELECTOR,"div.Home_FAQ__3uVm4 #accordion__heading-7[data-accordion-component='AccordionItemButton']")
ANSWER_DELIVERY_OUTSIDE_MKAD_DROPDOWN_MENU = (By.CSS_SELECTOR,"div.Home_FAQ__3uVm4 #accordion__panel-7[data-accordion-component='AccordionItemPanel'] p")
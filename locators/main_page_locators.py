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
QUESTION_PRICE_AND_PAYMENT_DROPDOWN_MENU = (By.XPATH,"//div[@data-accordion-component='AccordionItemButton' and normalize-space()='Сколько это стоит? И как оплатить?']")
ANSWER_PRICE_AND_PAYMENT_DROPDOWN_MENU = (By.XPATH,"//div[@data-accordion-component='AccordionItemPanel'][@aria-labelledby=//div[@data-accordion-component='AccordionItemButton' and normalize-space()='Сколько это стоит? И как оплатить?']/@id]//p")
# 2) Несколько самокатов
QUESTION_MULTIPLE_SCOOTERS_DROPDOWN_MENU = (By.XPATH,"//div[@data-accordion-component='AccordionItemButton' and normalize-space()='Хочу сразу несколько самокатов! Так можно?']")
ANSWER_MULTIPLE_SCOOTERS_DROPDOWN_MENU = (By.XPATH,"//div[@data-accordion-component='AccordionItemPanel'][@aria-labelledby=//div[@data-accordion-component='AccordionItemButton' and normalize-space()='Хочу сразу несколько самокатов! Так можно?']/@id]//p")
# 3) Расчёт времени аренды
QUESTION_RENT_TIME_CALCULATION_DROPDOWN_MENU = (By.XPATH,"//div[@data-accordion-component='AccordionItemButton' and normalize-space()='Как рассчитывается время аренды?']")
ANSWER_RENT_TIME_CALCULATION_DROPDOWN_MENU = (By.XPATH,"//div[@data-accordion-component='AccordionItemPanel'][@aria-labelledby=//div[@data-accordion-component='AccordionItemButton' and normalize-space()='Как рассчитывается время аренды?']/@id]//p")
# 4) Заказ на сегодня
QUESTION_ORDER_FOR_TODAY_DROPDOWN_MENU = (By.XPATH,"//div[@data-accordion-component='AccordionItemButton' and normalize-space()='Можно ли заказать самокат прямо на сегодня?']")
ANSWER_ORDER_FOR_TODAY_DROPDOWN_MENU = (By.XPATH,"//div[@data-accordion-component='AccordionItemPanel'][@aria-labelledby=//div[@data-accordion-component='AccordionItemButton' and normalize-space()='Можно ли заказать самокат прямо на сегодня?']/@id]//p")
# 5) Продление или ранний возврат
QUESTION_EXTEND_OR_RETURN_DROPDOWN_MENU = (By.XPATH,"//div[@data-accordion-component='AccordionItemButton' and normalize-space()='Можно ли продлить заказ или вернуть самокат раньше?']")
ANSWER_EXTEND_OR_RETURN_DROPDOWN_MENU = (By.XPATH,"//div[@data-accordion-component='AccordionItemPanel'][@aria-labelledby=//div[@data-accordion-component='AccordionItemButton' and normalize-space()='Можно ли продлить заказ или вернуть самокат раньше?']/@id]//p")
# 6) Зарядка в комплекте
QUESTION_CHARGER_INCLUDED_DROPDOWN_MENU = (By.XPATH,"//div[@data-accordion-component='AccordionItemButton' and normalize-space()='Вы привозите зарядку вместе с самокатом?']")
ANSWER_CHARGER_INCLUDED_DROPDOWN_MENU = (By.XPATH,"//div[@data-accordion-component='AccordionItemPanel'][@aria-labelledby=//div[@data-accordion-component='AccordionItemButton' and normalize-space()='Вы привозите зарядку вместе с самокатом?']/@id]//p")
# 7) Отмена заказа
QUESTION_ORDER_CANCELLATION_DROPDOWN_MENU = (By.XPATH,"//div[@data-accordion-component='AccordionItemButton' and normalize-space()='Можно ли отменить заказ?']")
ANSWER_ORDER_CANCELLATION_DROPDOWN_MENU = (By.XPATH,"//div[@data-accordion-component='AccordionItemPanel'][@aria-labelledby=//div[@data-accordion-component='AccordionItemButton' and normalize-space()='Можно ли отменить заказ?']/@id]//p")
# 8) Доставка за МКАД
QUESTION_DELIVERY_OUTSIDE_MKAD_DROPDOWN_MENU = (By.XPATH,"//div[@data-accordion-component='AccordionItemButton' and normalize-space()='Я жизу за МКАДом, привезёте?']")
ANSWER_DELIVERY_OUTSIDE_MKAD_DROPDOWN_MENU = (By.XPATH,"//div[@data-accordion-component='AccordionItemPanel'][@aria-labelledby=//div[@data-accordion-component='AccordionItemButton' and normalize-space()='Я жизу за МКАДом, привезёте?']/@id]//p")
from datetime import datetime, timedelta
import random

def get_next_day():
    """Функция для полчения следующего дня"""
    tomorrow = datetime.now() + timedelta(days=1)
    return tomorrow.strftime("%d.%m.%Y")

def generate_phone():
    """Функция для генерации номера"""
    return f"+7800{random.randint(1000000, 9999999)}"

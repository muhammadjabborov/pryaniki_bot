from aiogram.dispatcher.filters.state import StatesGroup, State


class Complain(StatesGroup):
    complaint = State()


class Order(StatesGroup):
    proudct_title = State()
    product_kilo = State()
    product_count = State()
    phone_number = State()
    address = State()


from aiogram.fsm.state import StatesGroup, State

# Состояния
class User(StatesGroup):
    text = State()
    send = State()

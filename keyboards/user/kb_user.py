
from aiogram import types


main_menu = [
    [types.InlineKeyboardButton(text='О зоопарке', callback_data='kb_about')],
    [types.InlineKeyboardButton(text='Проверить результаты', callback_data='get_results')],
    [types.InlineKeyboardButton(text='Начать викторину!', callback_data='victorina')],
]


about_menu = [
    [types.InlineKeyboardButton(text='Связаться с нами', callback_data='send_employee'),
     types.InlineKeyboardButton(text='Сайт', url='https://moscowzoo.moscow/')],
    [types.InlineKeyboardButton(text='Обратная связь', callback_data='feedback'),
     types.InlineKeyboardButton(text='В начало', callback_data='main_msgs')],
    [types.InlineKeyboardButton(text='Начать викторину!', callback_data='victorina')],
]


home_menu = [
    [types.InlineKeyboardButton(text='В начало', callback_data='main_msgs'),]
]


quest_menu = [
    [types.InlineKeyboardButton(text='В начало', callback_data='main_msgs')],
    [types.InlineKeyboardButton(text='A', callback_data='send_A'),
     types.InlineKeyboardButton(text='B', callback_data='send_B')],
    [types.InlineKeyboardButton(text='C', callback_data='send_C'),
     types.InlineKeyboardButton(text='D', callback_data='send_D')],
]


user_next = [
    [types.InlineKeyboardButton(text='Следующий вопрос', callback_data='victorina'),],
    [types.InlineKeyboardButton(text='В начало', callback_data='main_msgs'),]
]


see_result_victorina = [
    [types.InlineKeyboardButton(text='Посмотреть результат', callback_data='see_result_victorina'),],
    [types.InlineKeyboardButton(text='Начать заново!', callback_data='reset_results')],
    [types.InlineKeyboardButton(text='В начало', callback_data='main_msgs')],
]


user_reset = [
    [types.InlineKeyboardButton(text='Начать заново!', callback_data='reset_results'),],
    [types.InlineKeyboardButton(text='В начало', callback_data='main_msgs')],
]


main_menu = types.InlineKeyboardMarkup(inline_keyboard=main_menu)
about_menu = types.InlineKeyboardMarkup(inline_keyboard=about_menu)
home_menu = types.InlineKeyboardMarkup(inline_keyboard=home_menu)
quest_menu = types.InlineKeyboardMarkup(inline_keyboard=quest_menu)
see_result_victorina = types.InlineKeyboardMarkup(inline_keyboard=see_result_victorina)
user_next = types.InlineKeyboardMarkup(inline_keyboard=user_next)
user_reset = types.InlineKeyboardMarkup(inline_keyboard=user_reset)
from aiogram import types

admin_menu = [
    [types.InlineKeyboardButton(text='Список пользователей', callback_data='user_list')],
    [types.InlineKeyboardButton(text='Список отзывов', callback_data='feedback_list')],
    [types.InlineKeyboardButton(text='В начало', callback_data='main_msgs')],
]


admin_menu = types.InlineKeyboardMarkup(inline_keyboard=admin_menu)

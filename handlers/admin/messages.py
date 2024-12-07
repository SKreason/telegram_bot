import configparser
from asyncio import sleep

from aiogram import Dispatcher, types, F
from aiogram.filters import Command, BaseFilter
from aiogram.types import TelegramObject

from function.admin_options import get_user_list_db, get_feedback_list_db
from keyboards.admin.kb_admin import admin_menu

config = configparser.ConfigParser()
config.add_section('Settings')
config.read('config/config.ini')
ids = config['Settings']['admin']
admin_ids = ids.split(',')


# Проверка на права "admin"
class IsAdmin(BaseFilter):
    async def __call__(self, obj: TelegramObject) -> bool:
        id_user = str(obj.from_user.id)
        return id_user in admin_ids


# Меню администратора
async def cmd_admin(message: types.Message):
    await message.answer(
        'Добро пожаловать в админ панель!',
        reply_markup=admin_menu,
    )
    await sleep(0.3)


# Получение списка пользователей
async def get_user_list(callback: types.CallbackQuery):
    user_list = await get_user_list_db()
    await callback.message.answer(user_list, reply_markup=admin_menu)
    await sleep(0.3)


# Получение списка отзывов
async def get_feedback_list(callback: types.CallbackQuery):
    feedback_list = await get_feedback_list_db()
    await callback.message.answer(feedback_list, reply_markup=admin_menu)
    await sleep(0.3)


#Регистрация handlers
def register_admin_messages(dp: Dispatcher):
    dp.message.register(cmd_admin, F.text, Command('admin'), IsAdmin())
    dp.callback_query.register(get_user_list, F.data == 'user_list', IsAdmin())
    dp.callback_query.register(get_feedback_list, F.data == 'feedback_list', IsAdmin())

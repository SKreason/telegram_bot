import asyncio
from aiogram import Bot, Dispatcher
import logging

import configparser

from aiogram.client.default import DefaultBotProperties

from handlers.admin.messages import register_admin_messages
from handlers.user.messages import register_user_messages


logger = logging.getLogger(__name__)

# логирование работы бота, настройки логирования по ссылке https://docs.python.org/3/library/logging.html
logging.basicConfig(
        filename='my_bot.log',
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
logger.error("Starting bot")

config = configparser.ConfigParser()
config.add_section('Settings')
config.read('config/config.ini')
token = config.get('Settings', 'token')

bot = Bot(token, default=DefaultBotProperties(parse_mode='HTML'))

dp = Dispatcher()

async def main():
    register_admin_messages(dp)
    register_user_messages(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


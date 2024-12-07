from asyncio import sleep

from aiogram import types, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

from function.bot_elements import add_user, get_result, get_quest_victorina, get_quest_number, save_answer, \
    define_results, save_result, save_feedback, reset_results, send_employee

from keyboards.user.kb_user import main_menu, about_menu, home_menu, quest_menu, see_result_victorina, user_next, \
    user_reset

from states.state import User
from text.victorina_text import quest

from text.zoo_text import text_about, text_result1, text_result2, text_end_victorina, text_welcome, text_answer, \
    text_result_a, text_result_b, text_result_c, text_result_d, text_error, animal, text_feedback, text_reset, \
    text_employee, text_send_employee


#Запуск бота
async def cmd_start(message: types.Message,  state: FSMContext):
    await state.clear()
    await add_user(message.from_user.id, message.from_user.full_name, message.from_user.username)
    image_from_pc = FSInputFile("Image/image_main.jpg")
    await message.answer_photo(
        image_from_pc,
        caption=text_welcome,
        reply_markup=main_menu,
    )
    await sleep(0.3)


#Основное меню
async def main_msg(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    image_from_pc = FSInputFile("Image/image_main.jpg")
    await callback.message.answer_photo(
        image_from_pc,
        caption=text_welcome,
        reply_markup=main_menu,
    )
    await sleep(0.3)


#Меню "о зоопарке"
async def kb_about_handler(callback: types.CallbackQuery):
    image_from_pc = FSInputFile("Image/image_about.jpg")
    await callback.message.answer_photo(
        image_from_pc,
        caption=text_about,
        reply_markup=about_menu,
    )
    await sleep(0.3)


#Меню проверить результаты
async def get_result_handler(callback: types.CallbackQuery):
    image_from_pc1 = FSInputFile("Image/rez_out.jpg")
    image_from_pc2 = FSInputFile("Image/rez_in.jpg")
    user_rez = await get_result(callback.from_user.id)
    if user_rez == 0:
        await callback.message.answer_photo(
            image_from_pc1,
            text_result1,
            reply_markup=home_menu,
        )
    else:
        await callback.message.answer_photo(
            image_from_pc2,
            text_result2,
            reply_markup=see_result_victorina,
        )
    await sleep(0.3)


#Викторина
async def victorina_handler(callback: types.CallbackQuery):
    send_id = callback.from_user.id
    quest_number = await get_quest_number(send_id)
    quest_victorina, step_number = await get_quest_victorina(quest_number, send_id)
    if step_number <= len(quest):
        image_from_pc = FSInputFile(f"Image/number/{step_number}.jpg")
        await callback.message.answer_photo(
            image_from_pc,
            quest_victorina,
            reply_markup=quest_menu,
        )
    else:
        image_from_pc = FSInputFile(f"Image/end_vic.jpg")
        await define_results(send_id)
        await callback.message.answer_photo(
            image_from_pc,
            text_end_victorina,
            reply_markup=see_result_victorina,
        )
    await sleep(0.3)


#Ответ пользователя "Вариант А"
async def user_answer_a(callback: types.CallbackQuery):
    aw_user = "A"
    await save_answer(callback.from_user.id, aw_user)
    image_from_pc = FSInputFile("Image/answer.jpg")
    await callback.message.answer_photo(
        image_from_pc,
        text_answer,
        reply_markup=user_next,
    )
    await sleep(0.3)


#Ответ пользователя "Вариант B"
async def user_answer_b(callback: types.CallbackQuery):
    aw_user = "B"
    await save_answer(callback.from_user.id, aw_user)
    image_from_pc = FSInputFile("Image/answer.jpg")
    await callback.message.answer_photo(
        image_from_pc,
        text_answer,
        reply_markup=user_next,
    )
    await sleep(0.3)


#Ответ пользователя "Вариант C"
async def user_answer_c(callback: types.CallbackQuery):
    aw_user = "C"
    await save_answer(callback.from_user.id, aw_user)
    image_from_pc = FSInputFile("Image/answer.jpg")
    await callback.message.answer_photo(
        image_from_pc,
        text_answer,
        reply_markup=user_next,
    )
    await sleep(0.3)


#Ответ пользователя "Вариант D"
async def user_answer_d(callback: types.CallbackQuery):
    aw_user = "D"
    await save_answer(callback.from_user.id, aw_user)
    image_from_pc = FSInputFile("Image/answer.jpg")
    await callback.message.answer_photo(
        image_from_pc,
        text_answer,
        reply_markup=user_next,
    )
    await sleep(0.3)


#Меню получить/поделиться результаты викторины
async def see_result_victorina_handler(callback: types.CallbackQuery):
    send_id = callback.from_user.id
    result = await save_result(send_id)
    kb_send_tg = [
        [types.InlineKeyboardButton(
            text='Поделиться результатом в TG',
            url=f'https://t.me/share/url?url= '
                f'Я прошел викторину!\n'
                f'Мое тотемное животное - {animal[result]}.\n\n'
                f'Пройди и ты\n\n'
                f't.me/SKVtestBOT '), ],
        [types.InlineKeyboardButton(
            text='Поделиться результатом в Vk',
            url=f'https://vk.com/share.php?url='
                f'Я прошел викторину!\n'
                f'Мое тотемное животное - {animal[result]}.\n\n'
                f'Пройди и ты\n\n'
                f't.me/SKVtestBOT '),],
        [types.InlineKeyboardButton(text='Связаться с нами', callback_data='send_employee')],
        [types.InlineKeyboardButton(text='В начало', callback_data='main_msgs')],
    ]
    kb_send_tg = types.InlineKeyboardMarkup(inline_keyboard=kb_send_tg)
    if result == 1:
        image_from_pc = FSInputFile("Image/eagle.jpg")
        await callback.message.answer_photo(
            image_from_pc,
            text_result_a,
            reply_markup=kb_send_tg,
        )
    elif result == 2:
        image_from_pc = FSInputFile("Image/owl.jpg")
        await callback.message.answer_photo(
            image_from_pc,
            text_result_b,
            reply_markup=kb_send_tg,
        )
    elif result == 3:
        image_from_pc = FSInputFile("Image/dolphin.jpg")
        await callback.message.answer_photo(
            image_from_pc,
            text_result_c,
            reply_markup=kb_send_tg,
        )
    elif result == 4:
        image_from_pc = FSInputFile("Image/bear.jpg")
        await callback.message.answer_photo(
            image_from_pc,
            text_result_d,
            reply_markup=kb_send_tg,
        )
    else:
        image_from_pc = FSInputFile("Image/error.jpg")
        await callback.message.answer_photo(
            image_from_pc,
            text_error,
            reply_markup=user_reset,
        )
    await sleep(0.3)


#Меню отправки отзыва
async def set_feedback(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text="Напишите ваш отзыв", reply_markup=home_menu)
    await state.set_state(User.text)
    await sleep(0.3)


#Захват отзыва от пользователя
async def get_feedback(message: types.Message, state: FSMContext):
    user_feedback = message.text
    await state.clear()
    await save_feedback(user_feedback, message.from_user.id)
    image_from_pc = FSInputFile("Image/feedback.jpg")
    await message.answer_photo(
        image_from_pc,
        text_feedback,
        reply_markup=home_menu,
    )
    await sleep(0.3)


#Меню сброса результатов пользователя
async def user_reset_results(callback: types.CallbackQuery):
    await reset_results(callback.from_user.id)
    image_from_pc = FSInputFile("Image/complete.jpg")
    await callback.message.answer_photo(
        image_from_pc,
        text_reset,
        reply_markup=home_menu,
    )
    await sleep(0.3)


#Меню отправки сообщения сотруднику
async def send_message_employee(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text_employee,
        reply_markup=home_menu,
    )
    await sleep(0.3)
    await state.set_state(User.send)


#Захват сообщения для сотрудника
async def get_send(message: types.Message, state: FSMContext):
    user_message = message.text
    print(user_message)
    await state.clear()
    await send_employee(user_message, message.from_user.id)
    image_from_pc = FSInputFile("Image/message.jpg")
    await message.answer_photo(
        image_from_pc,
        text_send_employee,
        reply_markup=home_menu,
    )
    await sleep(0.3)


# Для ответа на любые сообщения пользователя вне запроса ввода
async def all_message(message: types.Message):
    image_from_pc = FSInputFile("Image/image_main.jpg")
    await message.answer_photo(
        image_from_pc,
        caption=text_welcome,
        reply_markup=main_menu,
    )
    await sleep(0.3)



#Регистрация handlers
def register_user_messages(dp: Dispatcher):
    dp.message.register(cmd_start, CommandStart())
    dp.message.register(get_send, User.send)
    dp.message.register(get_feedback, User.text)
    dp.message.register(all_message)
    dp.callback_query.register(kb_about_handler, F.data == 'kb_about')
    dp.callback_query.register(main_msg, F.data == 'main_msgs')
    dp.callback_query.register(get_result_handler, F.data == 'get_results')
    dp.callback_query.register(victorina_handler, F.data == 'victorina')
    dp.callback_query.register(user_answer_a, F.data == 'send_A')
    dp.callback_query.register(user_answer_b, F.data == 'send_B')
    dp.callback_query.register(user_answer_c, F.data == 'send_C')
    dp.callback_query.register(user_answer_d, F.data == 'send_D')
    dp.callback_query.register(see_result_victorina_handler, F.data == 'see_result_victorina')
    dp.callback_query.register(set_feedback, F.data == 'feedback')
    dp.callback_query.register(user_reset_results, F.data == 'reset_results')
    dp.callback_query.register(send_message_employee, F.data == 'send_employee')



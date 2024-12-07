import aiosqlite

from function.mail import send_mail
from text.victorina_text import quest
from text.zoo_text import animal


# Добавляем пользователя в базу для сбора статистики и сохранения результатов викторины.
async def add_user(user_id, full_name, username):
    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()
    check_user = await cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    check_user = await check_user.fetchone()
    if check_user is None:
        await cursor.execute('INSERT INTO users (my_bot.log) VALUES (?, ?, ?)',
                             (user_id, full_name, username))
        await cursor.execute('INSERT INTO results (user_id, result, quest_number) VALUES (?, ?, ?)',
                             (user_id, 0, 0))
        await connect.commit()
    await cursor.close()
    await connect.close()


# Получение результата викторины (бот сохраняет результаты викторины).
async def get_result(user_id):
    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()
    result_user = await cursor.execute('SELECT resultat FROM users WHERE user_id = ?', (user_id,))
    result_user = await result_user.fetchone()
    await cursor.close()
    await connect.close()
    return result_user[0]


# Получение номера текущего вопроса (бот сохраняет на каком вопросе остановился пользователь)
async def get_quest_number(user_id):
    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()
    quest_num = await cursor.execute('SELECT quest_number FROM results WHERE user_id = ?', (user_id,))
    quest_num = await quest_num.fetchone()
    await cursor.close()
    await connect.close()
    return quest_num[0]


# Получение вопроса для отправки пользователю, сохранение номера вопроса в базе.
async def get_quest_victorina(quest_number_send, send_id):
    if quest_number_send < len(quest):
        text = quest[quest_number_send]
        quest_number_send = quest_number_send + 1
        text_quest = f"Вопрос {quest_number_send}\n{text}"
        connect = await aiosqlite.connect('db.db')
        cursor = await connect.cursor()
        await cursor.execute('UPDATE results SET quest_number = ? WHERE user_id = ?', (quest_number_send, send_id))
        await connect.commit()
        await cursor.close()
        await connect.close()
        return text_quest, quest_number_send
    else:
        text_quest = "END"
        quest_number_send = 10
        return text_quest, quest_number_send


#Сохранение ответа пользователя в базу
async def save_answer(user_id, aw_user):
    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()
    answer = await cursor.execute('SELECT answer FROM results WHERE user_id = ?', (user_id,))
    code_answer = await answer.fetchone()
    quest_number = await cursor.execute('SELECT quest_number FROM results WHERE user_id = ?', (user_id,))
    quest_number = await quest_number.fetchone()
    if code_answer[0] is None and quest_number[0] == 1:
        await cursor.execute('UPDATE results SET answer = ? WHERE user_id = ?', (aw_user, user_id))
        await connect.commit()
    elif quest_number[0] == len(code_answer[0])+1:
        sv_answer = code_answer[0] + aw_user
        await cursor.execute('UPDATE results SET answer = ? WHERE user_id = ?', (sv_answer, user_id))
        await connect.commit()
    await cursor.close()
    await connect.close()


#Получение результата викторины по ответам из базы
async def define_results(user_id):
    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()
    answer = await cursor.execute('SELECT answer FROM results WHERE user_id = ?', (user_id,))
    answer = await answer.fetchone()
    answer = answer[0]
    answer_a = answer.count("A")
    answer_b = answer.count("B")
    answer_c = answer.count("C")
    answer_d = answer.count("D")
    if answer_a > answer_b and answer_a > answer_c and answer_a > answer_d:
        print("результат А")
        result = 1
        await cursor.execute('UPDATE results SET result = ? WHERE user_id = ?', (result, user_id))
        await connect.commit()
    elif answer_b > answer_c and answer_b > answer_d and answer_b > answer_a:
        print("результат B")
        result = 2
        await cursor.execute('UPDATE results SET result = ? WHERE user_id = ?', (result, user_id))
        await connect.commit()
    elif answer_c > answer_b and answer_c > answer_d and answer_c > answer_a:
        print("результат C")
        result = 3
        await cursor.execute('UPDATE results SET result = ? WHERE user_id = ?', (result, user_id))
        await connect.commit()
    elif answer_d > answer_a and answer_d > answer_b and answer_d > answer_c:
        print("результат D")
        result = 4
        await cursor.execute('UPDATE results SET result = ? WHERE user_id = ?', (result, user_id))
        await connect.commit()
    else:
        result = 8
        await cursor.execute('UPDATE results SET result = ? WHERE user_id = ?', (result, user_id))
        await connect.commit()
    await cursor.close()
    await connect.close()


#Сохранение результата викторины
async def save_result(user_id):
    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()
    result = await cursor.execute('SELECT result FROM results WHERE user_id = ?', (user_id,))
    result = await result.fetchone()
    result = result[0]
    await cursor.execute('UPDATE users SET resultat = ? WHERE user_id = ?', (result, user_id))
    await connect.commit()
    await cursor.close()
    await connect.close()
    return result


#Сохранение отзыва от пользователя в базу
async def save_feedback(user_feedback, user_id):
    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()
    await cursor.execute('INSERT INTO feedback_user (user_id, feedback) VALUES (?, ?)',
                             (user_id, user_feedback))
    await connect.commit()
    await cursor.close()
    await connect.close()


#Сброс результатов викторины для повторного прохождения
async def reset_results(user_id):
    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()
    await cursor.execute('UPDATE users SET resultat = ? WHERE user_id = ?', (0, user_id))
    await cursor.execute('UPDATE results SET result = ?, quest_number = ?, answer = ? WHERE user_id = ?',
                         (0, 0, None, user_id))
    await connect.commit()
    await cursor.close()
    await connect.close()


#Отправка сообщения сотруднику зоопарка на почту для связи
async def send_employee(message, user_id):
    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()
    result = await cursor.execute('SELECT result FROM results WHERE user_id = ?', (user_id,))
    result = await result.fetchone()
    result = result[0]
    user_result = animal[result]
    info = (f'Информация о пользователе:\n'
            f'id - {user_id}. \n'
            f'Результат викторины - {user_result}. \n'
            f'Сообщение - {message}.')
    await send_mail(info)
    await cursor.close()
    await connect.close()

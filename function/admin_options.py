import aiosqlite

from text.zoo_text import animal


#Генерация списка пользователей
async def get_user_list_db():
    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()
    list_user = await cursor.execute('SELECT * FROM users')
    list_user = await list_user.fetchall()
    max_id = len(list_user)
    text_list = []
    for i in range(max_id):
        user = (f'Id пользователя - {list_user[i][0]}\n'
            f'Имя пользователя - {list_user[i][1]}\n'
            f'Результат - {animal[list_user[i][3]]}\n')
        text_list.append(user)
    user_list = '\n'.join(text_list)
    await cursor.close()
    await connect.close()
    return user_list


# Генерация списка отзывов
async def get_feedback_list_db():
    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()
    list_feedback = await cursor.execute('SELECT * FROM feedback_user')
    list_feedback = await list_feedback.fetchall()
    max_i = len(list_feedback)
    text_list = []
    for i in range(max_i):
        feedback = (f'Id пользователя - {list_feedback[i][0]}\n'
                    f"""Отзыв - "{list_feedback[i][1]}"\n""")
        text_list.append(feedback)
    feedback_list = '\n'.join(text_list)
    await cursor.close()
    await connect.close()
    return feedback_list


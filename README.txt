Данный телеграмм бот разработан для сдачи задания по курсу Fullstack-разработчик Python Skillfactory.

Разработал Куряев Сергей Вячеславович.

Для работы запустить main.py

1. Бот создан с помощью BotFather в Telegram.

2. Бот запускается по команде /start. Есть возможность управления администраторами через команду /admin

3. Модуль викторины содержит 8 вопросов. На каждый вапрос есть 4 варианта ответа. Вопросы можно обновить и дополнить
через файл victorina_text.py

4. Реализован алгоритм обработки ответов и записи их в базу данных. Бот запоминает варианты и на каком вопросе
остановился пользователь. Пользователь всегда может вернуться к прохождению викторины.

5. Бот генерирует сообщение пользователю на основе результатов викторины. Предоставляет возможность ознакомиться с
программой опеки по ссылке.

6. Бот присылает к каждому сообщению картинку.

7. По итогу прохождения викторины можно поделиться результатом в VK и telegram. Сообщение генерируется на основе
результатов викторины прикрепляя ссылку на бота.

8. Есть возможность связаться с сотрудником путем отправки письма на электронную почту в формате - 
	Информация о пользователе: id - "xxx". Результат викторины - "xxx". Сообщение - "xxxxxx xxx".

9. В меню бота есть возможность перезапустить викторину и пройти заново.

10. Бот может собирать отзывы через меню обратной связи. Все отзывы заносятся в базу данных. Есть возможность вывода
списка отзывов через админ-панель.

11. Бот собирает минимальный объем личных данных (user_id, full_name, username). Список пользователей могут
просмотреть только администраторы бота.

12. Бот разработан на асинхронном фреймворке aiogram, позволяющим работать с большим количеством пользователей.

13. В боте реализовано логирование. Лог сохраняется в файл my_bot.log

14. Бот полностью сопровождает пользователя и корректно отрабатывает все команды от пользователя.


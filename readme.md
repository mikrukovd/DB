# Скрипт для правок в электронном дневнике
С помощью скрипта можно исправлять плохие оценки в электронном дневнике, удалять замечания, создавать похвалу. Все зависимости можно установить командой `pip install -r requirements.txt`. Версия `python 3.8.*`
## Как использовать
Файл необходимо скопировать в папку проекта и сделать импорт классов `Schoolkid`, `Mark`, `Chastisement`, `Lesson`, `Commendation`. По умолчанию импорт прописан из `datacenter.models`. 
## Описание `scripts.py`
- `get_student` ищет ученика в базе данных

- `fix_mark` исправляет все плохие оценки в дневнике на 5. Оценка считается плохой, если это 2 и 3. Ей необходимо передать ФИО ученика.

- `remove_chastisements` удаляет все замечания ученика. Ей необходимо передать ФИО ученика.

- `create_commendation` создает похвалу по предмету. Ей необходимо передать ФИО ученика и предмет. Комментарий похвалы выбирается из `COMMENDS`

## Пример использования
Есть сайт электронного дневника. Допустим мне потребовалось изменить некоторые данные, но на сайте это сделать нельзя. Для этого потребовалось подключится к базе данных через `Django shell`.
Для этого в терминал нужно ввести `python manage.py shell`. 

Мне известно имя ученика, у которого я хочу изменить данные, например я хочу удалить все замечания в дневнике. Для этого в терминал надо сделать импорт `from scripts import remove_chastisements`. Далее в терминале вызываю эту функцию и передаю ей ФИО ученика.
Если функция не показала ошибку, значит она сработала и данные в базе данных изменились.
## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [devman.org](https://dvmn.org)

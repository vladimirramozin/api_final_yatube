API для мини социальной сети.
Описание проекта:
Учебный проект по написанию API на основе DRF. 

Основные эндпоинты:
http://127.0.0.1:8000/api/v1/posts/ Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией.
http://127.0.0.1:8000/api/v1/posts/ Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.
http://127.0.0.1:8000/api/v1/posts/{id}/ Получение публикации по id.
http://127.0.0.1:8000/api/v1/posts/{id}/  Обновление публикации по id. Обновить публикацию может только автор публикации. Анонимные запросы запрещены.
http://127.0.0.1:8000/api/v1/posts/{id}/ Частичное обновление публикации по id. Обновить публикацию может только автор публикации. Анонимные запросы запрещены.
http://127.0.0.1:8000/api/v1/posts/{id}/ Удаление публикации по id. Удалить публикацию может только автор публикации. Анонимные запросы запрещены.
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/ Получение всех комментариев к публикации.
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/ Добавление нового комментария к публикации. Анонимные запросы запрещены.
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/ Получение комментария к публикации по id.
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/ Обновление комментария к публикации по id. Обновить комментарий может только автор комментария. Анонимные запросы запрещены.
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/ Частичное обновление комментария к публикации по id. Обновить комментарий может только автор комментария. Анонимные запросы запрещены.
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/ Удаление комментария к публикации по id. Обновить комментарий может только автор комментария. Анонимные запросы запрещены.
http://127.0.0.1:8000/api/v1/groups/ Получение списка доступных сообществ.
http://127.0.0.1:8000/api/v1/groups/{id}/ Получение информации о сообществе по id.
http://127.0.0.1:8000/api/v1/follow/ Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены.
http://127.0.0.1:8000/api/v1/follow/ Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса. Анонимные запросы запрещены.
http://127.0.0.1:8000/api/v1/jwt/create/ Получение JWT-токена.
http://127.0.0.1:8000/api/v1/jwt/refresh/ Обновление JWT-токена.
http://127.0.0.1:8000/api/v1/jwt/verify/ Проверка JWT-токена.


Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/vladimirramozin/api_final_yatube.git
cd api_final_yatube
Cоздать и активировать виртуальное окружение:

python3 -m venv env
source .venv/bin/activate
Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip
pip install -r requirements.txt
Выполнить миграции:

python3 manage.py migrate
Запустить проект:

python3 manage.py runserver

Пример запроса:
{
"text": "sterwsfdrifddxvcng"
}

Системные требования:
Python 3.7
Django==2.2.16
pytest==6.2.4
pytest-pythonpath==0.7.3
pytest-django==4.4.0
djangorestframework==3.12.4
djangorestframework-simplejwt==4.7.2
Pillow==8.3.1
PyJWT==2.1.0
requests==2.26.0

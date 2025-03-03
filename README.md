Yatube API

Yatube API — это RESTful API для социальной сети, где пользователи могут публиковать посты, комментировать их, подписываться на других пользователей и взаимодействовать с группами. API поддерживает JWT-аутентификацию и предоставляет доступ к данным через стандартные HTTP-методы.
Основные возможности

    Посты:

        Получение списка всех постов с пагинацией.

        Создание, редактирование и удаление постов.

        Добавление изображений к постам.

    Комментарии:

        Получение списка комментариев к посту.

        Создание, редактирование и удаление комментариев.

    Группы:

        Получение списка всех групп.

        Получение информации о конкретной группе.

    Подписки:

        Получение списка подписок текущего пользователя.

        Подписка на других пользователей.

    Аутентификация:

        Получение JWT-токена для доступа к API.

        Обновление и проверка токенов.

Установка и запуск

    Клонируйте репозиторий:
    bash
    Copy

    git clone https://github.com/ваш-username/yatube-api.git
    cd yatube-api

    Создайте виртуальное окружение и установите зависимости:

    python -m venv venv
    source venv/bin/activate  # Для Linux/MacOS
    venv\Scripts\activate     # Для Windows
    pip install -r requirements.txt

    Примените миграции:

    python manage.py migrate

    Создайте суперпользователя (опционально):

    python manage.py createsuperuser

    Запустите сервер:

    python manage.py runserver

Использование API
Базовый URL

Все запросы к API выполняются по базовому URL:

http://localhost:8000/api/v1/

Аутентификация

Для доступа к защищённым эндпоинтам необходимо получить JWT-токен.
Получение токена:

    URL: /api/v1/jwt/create/

    Метод: POST

    Тело запроса:
    json
    Copy

    {
      "username": "ваш_username",
      "password": "ваш_password"
    }

    Ответ:
    json
    Copy

    {
      "refresh": "ваш_refresh_токен",
      "access": "ваш_access_токен"
    }

Обновление токена:

    URL: /api/v1/jwt/refresh/

    Метод: POST

    Тело запроса:
    json
    Copy

    {
      "refresh": "ваш_refresh_токен"
    }

    Ответ:
    json
    Copy

    {
      "access": "новый_access_токен"
    }

Проверка токена:

    URL: /api/v1/jwt/verify/

    Метод: POST

    Тело запроса:
    json
    Copy

    {
      "token": "ваш_access_или_refresh_токен"
    }

Эндпоинты
Посты

    Получение списка постов:

        URL: /api/v1/posts/

        Метод: GET

        Параметры:

            limit (опционально): Количество постов на страницу.

            offset (опционально): Номер страницы.

    Создание поста:

        URL: /api/v1/posts/

        Метод: POST

        Тело запроса:
        json
        Copy

        {
          "text": "Текст поста",
          "group": 1,  # Опционально
          "image": "base64_encoded_image"  # Опционально
        }

    Получение поста по ID:

        URL: /api/v1/posts/{id}/

        Метод: GET

    Редактирование поста:

        URL: /api/v1/posts/{id}/

        Метод: PUT/PATCH

    Удаление поста:

        URL: /api/v1/posts/{id}/

        Метод: DELETE

Комментарии

    Получение списка комментариев:

        URL: /api/v1/posts/{post_id}/comments/

        Метод: GET

    Создание комментария:

        URL: /api/v1/posts/{post_id}/comments/

        Метод: POST

        Тело запроса:
        json
        Copy

        {
          "text": "Текст комментария"
        }

    Редактирование комментария:

        URL: /api/v1/posts/{post_id}/comments/{id}/

        Метод: PUT/PATCH

    Удаление комментария:

        URL: /api/v1/posts/{post_id}/comments/{id}/

        Метод: DELETE

Группы

    Получение списка групп:

        URL: /api/v1/groups/

        Метод: GET

    Получение информации о группе:

        URL: /api/v1/groups/{id}/

        Метод: GET

Подписки

    Получение списка подписок:

        URL: /api/v1/follow/

        Метод: GET

    Подписка на пользователя:

        URL: /api/v1/follow/

        Метод: POST

        Тело запроса:
        json
        Copy

        {
          "following": "username_пользователя"
        }

Примеры запросов
Получение списка постов

curl -X GET http://localhost:8000/api/v1/posts/

Создание поста

curl -X POST http://localhost:8000/api/v1/posts/ \
-H "Authorization: Bearer ваш_access_токен" \
-H "Content-Type: application/json" \
-d '{"text": "Новый пост", "group": 1}'

Подписка на пользователя

curl -X POST http://localhost:8000/api/v1/follow/ \
-H "Authorization: Bearer ваш_access_токен" \
-H "Content-Type: application/json" \
-d '{"following": "username_пользователя"}'


Автор

    Сергей Крюк

    GitHub: SERG-KRUK

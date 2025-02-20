# api_final
# Описание
Данный проект является REST API для проекта yatube, что позволит использовать его для взаимодействия с другими приложениями и сервисами.
Реализовано разделение доступа: аутентифицированные пользователи могут создавать, изменять и удалять свой контент. Неаутентифицированные пользователи имеют доступ только на чтение.

# Установка
### Чтобы развернуть проект на локальной машине необходмо выполнить следующее:
#### 1) Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/AlenaLezzhova/api_final_yatube
```
#### 2) Перейти в каталог с проектом:
```
cd api_final_yatube
```
#### 3) Создать виртуальное окружение:
```
py -3.7 -m venv venv
```
#### 4) Активировать виртуальное окружение:
```
source venv/Scripts/activate
```
#### 5) Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
python pip install -r requirements.txt
```
#### 6) Выполнить миграции:
```
python manage.py makemigrations
python manage.py migrate
```
#### 7) Запустить проект:
```
python manage.py runserver
```

# Примеры
### Некоторые примеры запросов к API.

#### 1) POST-запрос на http://127.0.0.1:8000/auth/users/ для создания пользователя:
```
{
    "username": "admin",
    "password": "pswrd123!"
}
```

#### 2) POST-запрос на http://127.0.0.1:8000/auth/jwt/create/ для получения токена для дальнейшей работы с API, где admin и pswrd123!- данные созданного ранее пользователя:
```
{
    "username": "admin",
    "password": "pswrd123!"
}
```
#### 3) GET-запрос на http://127.0.0.1:8000/api/v1/posts/ для получения всех постов.
#### 4) GET-запрос на http://127.0.0.1:8000/api/v1/posts/{id}/ для получения поста с указанным id.
#### 5) POST-запрос на http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/ для создания комментария к посту с id = post_id. Важно: использовать токен.
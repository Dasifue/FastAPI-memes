# Meme FastAPI

## Проект для технического задания
## Введение

Проект представляет из себя REST API сервис для работы с мемами. Сервис позволяет получить список мемов, получить один мем, создавать, обновлять и удалять уже существующие мемы.

Также имеется система авторизации через JWT токены, передаваемые через cookie

### Основной функционал <br>
(url адреса для локальной машины)


1. Регистрация (POST)
```
http://127.0.0.1:8000/auth/register
```

2. Авторизация (POST)
```
http://127.0.0.1:8000/auth/jwt/login
```
3. Логаут (POST)
```
http://127.0.0.1:8000/auth/jwt/logout
```
4. Список мемов (GET)
```
http://127.0.0.1:8000/memes/
```
5. Один экземпляр мема (GET)
```
http://127.0.0.1:8000/memes/{id}
```
6. Создание мема (POST)
```
http://127.0.0.1:8000/memes/
```
7. Обновление мема (PUT)
```
http://127.0.0.1:8000/memes/{id}
```
8. Удаление мема (DELETE)
```
http://127.0.0.1:8000/memes/{id}
```
9. Получение картинки мема (GET)
```
http://127.0.0.1:8000/media/{name}
```

Для большей информации о каждом эндпоинте можно воспользоваться документацией, сгенерированной с помощью **Swagger**

GET
```
http://127.0.0.1:8000/
```

### Использованные инструменты

1. Python 3.12
2. FastAPI
3. PostgreSQL
4. SQLAlchemy
5. Alembic
6. Minio
7. Docker, docker compose

## Установка и запуск

1. Клонируйте гит репозиторий и войдите в директорию
```bash
git clone https://github.com/Dasifue/FastAPI-memes.git

cd FastAPI-memes
```

## Для пользования через Docker

2. Убедитесь, что у вас установлен Docker и docker compose
https://docs.docker.com/engine/install/  - Docker
https://docs.docker.com/compose/install/ - Docker compose

3. Создайте файл ```.env.docker```. Скопируйте содержимое ```.env.example``` в файл и передайте значения пустым переменным <br>
Задайте значения для переменных:
```
DB_HOST = db
MINIO_HOST = minio
```

4. 1. Билд и запуск контейнеров
```bash
docker-compose up --build
```

4. 2. Билд и запуск в фоновом режиме
```bash
docker-compose up --build -d
```

5. Авторизуйтесь в minio по url адресу <br>
Логин и пароль вы задаёте в .env.docker
```
http://192.168.0.106:9001/login
```

6. Создайте бакет **memes**
```
http://192.168.0.106:9001/buckets
```

7. Создайте ключи доступа (ключи должны быть идентичны ключам из .env.docker)
```
http://192.168.0.106:9001/access-keys
```

8. Перейдите по url адресу и установка завершена
```
http://127.0.0.1:8000/
```

## Для локального использования

2. Создайте виртуальное окуржение и активируйте его
<br> Для Unix
```bash
python3.12 -m venv venv

source venv/bin/activate
```
Для Windows
```
python -m venv venv

./venv/Scripts/activate
```

3. Установите все зависисмости
```bash
pip install -r requirements.txt
```

4. Создайте ```.env``` файл, по примеру ```.env.example``` файла. Необходимо заранее создать базу данных и пользователя с паролем в **PostgreSQL** и бакет с ключами доступа в **Minio**. Заполните пустые переменные

5. Примените миграции в базу данных
```bash
alembic upgrade head
```

6. Запуск проекта
```bash
fastapi dev
```
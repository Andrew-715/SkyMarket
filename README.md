# Сайт объявлений Small_Market (backend)
____
### Cтек приложения:
- **Python 3.10**
- **Django**
- **Postgres SQL**
- **Docker**
- **CSS, JavaScript, SCSS (образ для фронта был взят [отсюда](https://github.com/skypro-008/coursework_6_skymarket/tree/main/frontend_react))**
____
### Подготовка и запуск приложения:
1. **Клонирование приложения.**
   1. В консоли иcпользуйте команду `git clone https://github.com/Andrew-715/SkyMarket.git`
2. **Создание виртуального окружения.**
   1. В консоли используйте команду в директории проекта`python -m venv venv`
3. **Установка зависимостей.**
   1. В консоли используйте команду `pip install -r requirements.txt`
4. **Создание docker-образа.**
   1. Перейдите в директорию "market_postgres".
   2. В консоли используйте команду `docker-compose up --build -d`
6. **Запуск.**
   1. Перейдите в директорию "skymarket".
   2. В консоли используйте команду `python ./manage.py runserver`
____

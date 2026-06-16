# CinemaWorld 🎬

Финальный проект системы управления кинотеатром на Django.

## ✨ Основные фичи
* **config/** — главное корневое приложение проекта.
* **apps/movies/** — логика фильмов (названия, постеры, трейлеры)
* **apps/promotions/** — управление акциями, скидками и баннерами.
* **apps/halls/** — логика зала, тип зала, схема
* **apps/session/** — логика сеансов, залов, расписаний
* Чистая структура проекта (все кастомные приложения изолированы в папке `apps/`).

##  Технологии
* Python 3
* Django
* Pillow

##  Как запустить локально


1. Клонировать репозиторий:
```bash
git clone [https://github.com/yatoo8/CinemaWorld.git](https://github.com/yatoo8/CinemaWorld.git)
cd CinemaWorld

# Как запустить

# 1. Создать виртуальное окружение:
python -m venv venv .
source venv/bin/activate


# 2. Установить зависимости:
pip install -r requirements.txt

# 3. Выполнить миграции:
python manage.py makemigrations
python manage.py migrate

# 4. Запустить сервер:
python manage.py runserver
Инструменты разработки
Стек:

Python == 3.11
Django == 4.2.3
sqlite3
Разработка
1) Клонировать репозиторий
git clone https://github.com/Gry-95/test_task_menu.git
2) Создать виртуальное окружение
cd django_menu

python -m venv venv
3) Активировать виртуальное окружение
Linux

source venv/bin/activate
Windows

./venv/Scripts/activate
4) Устанавливить зависимости:
pip install django == 4.2.3
5) Выполнить команду для выполнения миграций
python manage.py migrate
6) Создать суперпользователя
python manage.py createsuperuser
7) Запустить сервер
python manage.py runserver
10) Ссылки
Сайт http://127.0.0.1:8000/

Админ панель http://127.0.0.1:8000/admin
### Инструменты разработки
### Стек:

Python == 3.11

Django == 4.2

sqlite3

### Разработка:
#### Клонировать репозиторий 


    git clone https://github.com/Gry-95/test_task_menu.git

#### Создать виртуальное окружение


    cd django_menu

    python -m venv venv


#### Активировать виртуальное окружение


    Linux

    source venv/bin/activate
    
    Windows

    ./venv/Scripts/activate

#### Устанавливить зависимости:


    pip install django == 4.2.3

#### Выполнить команду для выполнения миграций


    python manage.py migrate

#### Создать суперпользователя


    python manage.py createsuperuser
#### Запустить сервер


    python manage.py runserver
#### Ссылки


    Сайт http://127.0.0.1:8000/

    Админ панель http://127.0.0.1:8000/admin
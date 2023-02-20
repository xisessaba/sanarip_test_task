1. Для начала создаем виртуальное окружение  python3 -m venv 'names virtual'
2. Активируем наше виртуальное окружение 
                                        ubuntu: source venv/bin/activate
                                        windows: venv/Scripts/activate

3. Установливаем наши пакеты. Вводим команду pip install -r requirements.txt
4. Создаем базу данных postgresql 
                                ubuntu: открываем терминал пишем команду sudo -u postgres psql , а затем пишем create database 'names database';
                                windows: открываем pgadmin и создаем новую базу данных 
4.1 в .env пишем свои данные 

5. Проводим миграцию командой python manage.py makemigrations, а затем python manage.py migrate

6. Создаем супер пользователя командой python manage.py createsuperuser

7. Запускаем проект командой python manage.py runserver 0.0.0.0:8000





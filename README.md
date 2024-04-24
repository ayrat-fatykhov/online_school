# Проект онлайн-школы

## Команда для запуска приложения
python3 manage.py runserver

## Запросы в Postman для курса
POST: http://localhost:8000/course/ (заполнить тело, выбрав параметры 'raw' и 'json'; поля: name, description)
GET: http://localhost:8000/course/<pk курса>/
PUT: http://localhost:8000/course/<pk курса>/ (заполнить тело, выбрав параметры 'raw' и 'json')
DELETE: http://localhost:8000/course/<pk курса>/

## Запросы в Postman для урока
POST: http://localhost:8000/lesson/create/ (заполнить тело, выбрав параметры 'raw' и 'json', поля: name, description, course)
GET (получить список уроков): http://localhost:8000/lesson/list/ 
GET (получить конкретный урок): http://localhost:8000/lesson/view/<pk урока>/
PATCH: http://localhost:8000/lesson/update/<pk урока>/
DELETE: http://localhost:8000/lesson/delete/<pk урока>/

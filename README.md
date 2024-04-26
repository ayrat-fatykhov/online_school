# Проект онлайн-школы

## Команда для запуска приложения
python3 manage.py runserver

## 24.1 Вьюсеты и дженерики
### Запросы в Postman для курса
POST: http://localhost:8000/course/ (заполнить тело, выбрав параметры 'raw' и 'json'; поля: name, description)
GET: http://localhost:8000/course/<pk курса>/
PUT: http://localhost:8000/course/<pk курса>/ (заполнить тело, выбрав параметры 'raw' и 'json')
DELETE: http://localhost:8000/course/<pk курса>/

### Запросы в Postman для урока
POST: http://localhost:8000/lesson/create/ (заполнить тело, выбрав параметры 'raw' и 'json', поля: name, description, course)
GET (получить список уроков): http://localhost:8000/lesson/list/ 
GET (получить конкретный урок): http://localhost:8000/lesson/view/<pk урока>/
PATCH: http://localhost:8000/lesson/update/<pk урока>/
DELETE: http://localhost:8000/lesson/delete/<pk урока>/

## 24.2 Сериализаторы
### Запросы в Postman для курса
GET: http://localhost:8000/course/

### Запросы в Postman для пользователя
GET (фильтровать по способу оплаты): http://localhost:8000/users/payment/list/?pay_approach=<значение> (в базе данных имеются str значения: 'наличными' и 'картой')
GET (фильтровать по  курсу): http://localhost:8000/users/payment/list/?payed_course=<значение> (в базе данных имеются int значения: 2 и 3)

### Примечания
Заполнение базы данных произведено в админке.
Для создания суперпользователя создана кастомная команда 'python3 manage.py csu'.
Для заполнения базы данных можно воспользоваться командой 'python3 manage.py loaddata db.json'.
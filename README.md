#YaMDb
Проект YaMDb собирает отзывы и оценки пользователей на различные произведения. 
Произведения делятся на различные категории и жанры.
Пользователь может оставить свой отзыв/оценку или посмотреть рейтинг 
(составленный из оценок пользователей)
какого-либо произведения

## Технологии и требования
```
Python 3.9+
Django
Django REST Framework
```

## Запуск проекта

```
1) Скачать проект с гитхаб

2) Установить зависимости:
python -m pip install --upgrade pip
pip install -r requirements.txt

3) Создать и применить миграции:
python manage.py makemigrations
python manage.py migrate

4) Заполнение файла .env
EMAIL_HOST = 
EMAIL_PORT = 
EMAIL_HOST_USER = 
EMAIL_HOST_PASSWORD = 

5) Запустить проект:
python manage.py runserver
```

# Sample Todo API Django

## How to Install

1. Git Clone

```
git clone git@github.com:panhavoan-leng/sample-todo-app.git
```

2. Backend setting

```
cd backend
python3 -m venv env
(For Mac) source env/bin/activate
(For Windows) env/Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser
# Open http://127.0.0.1:8000/todos/
```

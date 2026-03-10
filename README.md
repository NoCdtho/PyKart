# Pykart

Build simple website with the help of bootstrap, django framework and database dbsqlite3.

Programming Languages used here are html, little javascript and mostly python.

It is just learner project to see how django framework works.

what's happening in this project:-->
1) Fired up the django project:(django-admin startproject project_name)
2) local hosted using command (python manage.py runserver)
3) And whenever I add a product in this link http://127.0.0.1:8000/admin/
   I can show the product in this url http://127.0.0.1:8000/products/
   Basically build two apps one for adding the items and other one for showing those products dynamically no
   need to change code.

Key features:-->
Dynamic Content: Products added via the Django Admin panel are automatically reflected on the frontend.
Responsive Design:Styled using Bootstrap 5 for a mobile-friendly experience.
Database Integration: Uses SQLite3 for lightweight data management.
Admin Control: Full CRUD (Create, Read, Update, Delete) capabilities through the `/admin` dashboard.


Run locally:-->
1. clone the repo.
2. python -m venv venv (Create the environment)
   venv\Scripts\activate (Activate it (Windows))
3. pip install django
4. python manage.py makemigrations
   python manage.py migrate
5. python manage.py createsuperuser
6. python manage.py runserver

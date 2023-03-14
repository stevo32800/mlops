1.create project: django-admin startprojet ia4all

2.create app: django-admin startapp authentification prediction

3.dans install app dans le settings.py du projet rajouter les nouvelles apps:
INSTALLED_APPS = 'authentification', 'application'

cre

Pour chaque update: 
python manage.py makemigrations authentification

pour crer l'espace utilisateur
python manage.py createsuperuser
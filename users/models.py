from django.db import models

# / - домашняя страница () <страница с контактами, ответы на вопросы, страница со списком польз.>
# /contact - страница с контактами () <домашняя страница>
# /faq - ответы на вопросы () <домашняя страница>
# /users/list - страница со списком пользователей(users: list) <домашняя страница, информация о польз.>
# /users/<int:id>/ - информация о выбранном пользователе(user: User) <страницу со списком пользователей>

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField(default=0)
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, default='')
    phone = models.CharField(max_length=25, default='')

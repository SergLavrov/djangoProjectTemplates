from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import User

# / - домашняя страница () <страница с контактами, ответы на вопросы, страница со списком польз.>
# /contact - страница с контактами () <домашняя страница>
# /faq - ответы на вопросы () <домашняя страница>
# /users/list - страница со списком пользователей(users: list) <домашняя страница, информация о польз.>
# /users/<int:id>/ - информация о выбранном пользователе(user: User) <страницу со списком пользователей>

# Create your views here.


def register(request: HttpRequest) -> HttpResponse:
    try:
        user = User(name='Alex', age=20, city='Moscow', email='alex@mai.ru', phone='417-25-89')
        user1 = User(name='Fill', age=25, city='Brest', email='fill@mai.ru', phone='917-25-99')
        user2 = User(name='Vlad', age=21, city='Vitebsk', email='vlad@gmai.ru', phone='715-55-10')
        user3 = User(name='Ivan', age=30, city='Piter', email='vano@mai.ru', phone='546-05-00')
        user4 = User(name='Nazar', age=27, city='Moscow', email='nz@mai.ru', phone='917-66-87')
        list_users = [user, user1, user2, user3, user4]
        for user in list_users:
            user.save()
        return HttpResponse("OK")
    except:
        return HttpResponse("Error")


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Response from django")

def test_template(request: HttpRequest) -> HttpResponse:
    user = User.objects.get(id=1)
    template = loader.get_template('test.html')
    data = {
        'header': user.name,
        'somedata1': user.email,
        'somedata2': user.phone,
    }
    return HttpResponse(template.render(data))


def list_requests(request: HttpRequest) -> HttpResponse:
    users = User.objects.all().values()
    template = loader.get_template('table_list.html')
    data = {
        'header': 'Пользователи',
        'users': users,
    }
    return HttpResponse(template.render(data))


def get_user_profile(request: HttpRequest, id: int) -> HttpResponse:
    try:
        user = User.objects.get(id=id)
        template = loader.get_template('user_profile.html')
        data = {
            'header': 'Профиль пользователя',
            'user': user,
        }
        return HttpResponse(template.render(data, request))
    except:
        return HttpResponse("Error")


def list_contacts(request: HttpRequest) -> HttpResponse:
    users = User.objects.all().values()
    template = loader.get_template('contacts.html')
    data = {
        'header': 'Contacts of users',
        'users': users,
    }
    return HttpResponse(template.render(data))

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='users-register'),
    path('', views.home, name='users-home'),
    path('test_template/', views.test_template, name='users-test_template'),
    path('list_requests/', views.list_requests, name='users-list_requests'),
    path('get_user_profile/<int:id>/', views.get_user_profile, name='users-get_user_profile'),
    path('list_contacts/', views.list_contacts, name='users-list_contacts'),
]

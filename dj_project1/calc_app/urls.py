from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='add'),
    path('signin', views.signin, name='signin'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('update', views.update, name='update-account'),
    path('delete', views.deletion, name='delete-account'),

]

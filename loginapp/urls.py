from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index,name='index'),
    path("contact/",views.contact,name="contact"),
    path("login/",views.login,name="login"),
    path("register/",views.register,name="register"),
    path("logout/",views.logout,name="logout"),
]
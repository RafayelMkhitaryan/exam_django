from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'polls'
urlpatterns = [
    path("", views.index, name="index"),
    path("course/<int:course_id>/", views.course_detail, name="course_detail"),
    path("course/<int:course_id>/rate/", views.rate_course, name="rate_course"),
    path("login/", views.login, name = "login"),
    path("register/", views.register, name="register"),

]
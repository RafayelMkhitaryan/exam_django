from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect

from .models import Course, Lecture

def index(request):
    courses = Course.objects.all()
    return render(request, '/polls/index.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, "polls/course_detail.html", {"course": course})

def rate_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == "POST":
        try:
            new_rating = float(request.POST["rating"])
            course.update_rating(new_rating)
            return redirect("course_detail", course_id=course_id)
        except ValueError:
            return render(request, "polls/rate_course.html", {
                "course": course,
                "error_message": "Invalid rating.",
            })
    return render(request, "polls/rate_course.html", {"course": course})

def register(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repeat_password = request.POST["repeat_password"]
        email = request.POST["email"]

        if password != repeat_password:
            return render(request, "polls/register.html", {"error massage": "Password do not match"})

        user = User.objects.create_user(username=email, email=email, password=password)
        user.firstname = firstname
        user.lastname = lastname
        user.save()

        return HttpResponseRedirect('login')
    else:
        return render(request, "polls/register.html", {})


def login(request):
    if request.method == "GET":
        return render(request, 'polls/login.html', {})
    else:
        try:
            email = request.POST["email"]
            password = request.POST["password"]
        except:
            return render(request, "polls/login.html", {"error_message": "Missed Field"})

    user = authenticate(username=email, password=password)
    print("USER", email, password)
    if user:
        login(request)
        return HttpResponseRedirect('/polls/')
    else:
        return render(request, "polls/login.html", {"error_message": "Email or password is incorrect."})

def logout(request):
    logout(request)
    return HttpResponseRedirect("/polls/login")
# Create your views here.


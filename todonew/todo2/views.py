from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Tasks


# Create your views here.


class Tasklist(ListView):
    model = Tasks
    context_object_name = 'tasks'
    template_name = 'task-list.html'


class TaskCreate(CreateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    template_name = 'task-create.html'


class TaskUpdate(UpdateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    template_name = 'task-create.html'


class TaskDelete(DeleteView):
    model = Tasks
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')
    template_name = 'task-delete.html'


class TaskDetail(DetailView):
    model = Tasks
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')
    template_name = 'task-detail.html'


def home_fun(request):
    return render(request,'home.html')

def register_fun(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)

        myuser.save()

        return redirect('login')

    return render(request, 'register.html')


def login_fun(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.username
            return render(request, 'task-list.html', {'fname': fname})

        else:
            return redirect('login')

    return render(request, 'login.html')

def signout(request):
    logout(request)
    messages.success(request, 'Logged out Successfully!')
    return redirect('login')
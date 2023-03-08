from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import RegisterForm, LoginForm
from .models import Tasks, Register, Login


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
    regggister = Register.objects.all()
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/login')

    context={'register':regggister,'form':form}
    return render(request, "register.html",context)


def login_fun(request):
    logggin = Login.objects.all()
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/task-list')

    context={'login':logggin,'form':form}
    return render(request, "login.html",context)

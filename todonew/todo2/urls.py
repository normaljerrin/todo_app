from django.urls import path
from . import views
from .views import Tasklist, TaskCreate, TaskUpdate, TaskDelete, TaskDetail

urlpatterns = [
    path('task-list', Tasklist.as_view(), name='tasks'),
    path('task-create', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('task-detail/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('register',views.register_fun,name='register'),
    path('login',views.login_fun,name='login'),
    path('',views.home_fun,name='home'),
    ]
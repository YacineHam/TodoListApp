from django.urls import path
from .views import TaskDeleteView, RegistrationView,LoginView,TaskDetailView, TaskListView,TaskCreateView,TaskUpdateView,TaskDeleteView
from django.contrib.auth.views import LogoutView, redirect_to_login
urlpatterns = [
    path('',TaskListView.as_view(),name="taskList"),
    path('detail/<int:pk>/',TaskDetailView.as_view(),name='taskDetail'),
    path('task-create/',TaskCreateView.as_view(),name='taskCreate'),
    path('task-update/<int:pk>/',TaskUpdateView.as_view(),name='taskUpdate'),
    path('task-delete/<int:pk>/',TaskDeleteView.as_view(),name='taskDelete'),
    path('login/',LoginView.as_view(),name="login"),
    path('lougout/',LogoutView.as_view(next_page = "login"),name='logout'),
    path('signup/',RegistrationView.as_view(),name='register')

]

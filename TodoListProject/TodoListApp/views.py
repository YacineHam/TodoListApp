from django.http import request
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from .models import Task
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView,DeleteView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class LoginView(LoginView):
    template_name = 'TodoListApp/login.html'
    redirect_authenticated_user = True
    fields = '__all__'
    
    def get_success_url(self):
        return reverse_lazy("taskList")
    
class RegistrationView(FormView):
    template_name = 'TodoListApp/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url =reverse_lazy("taskList")
    
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super().form_valid(form)
    
    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('taskList')
        return super().get(*args, **kwargs)




class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = "tasks"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks']=context['tasks'].filter(user=self.request.user)
        context['count']=context['tasks'].filter(completed=True).count()     
        search = self.request.GET.get('search-area') or ''
        if search:
            context['tasks']=context['tasks'].filter(title__icontains=search)
            context['search'] ='true'
        return context
    
    
class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    
class TaskCreateView(CreateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('taskList')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('taskList')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('author-list')
    context_object_name = 'task'
    success_url = reverse_lazy('taskList')




    





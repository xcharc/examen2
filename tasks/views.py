from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import PendingTask

def list_ids(request):
    tasks = PendingTask.objects.all().values_list('api_id', flat=True)
    return render(request, 'tasks/list_ids.html', {'tasks': tasks})

def list_ids_titles(request):
    tasks = PendingTask.objects.all()
    return render(request, 'tasks/list_ids_titles.html', {'tasks': tasks})

def list_unresolved(request):
    tasks = PendingTask.objects.filter(completed=False)
    return render(request, 'tasks/list_unresolved.html', {'tasks': tasks})

def list_resolved(request):
    tasks = PendingTask.objects.filter(completed=True)
    return render(request, 'tasks/list_resolved.html', {'tasks': tasks})

def list_ids_user(request):
    tasks = PendingTask.objects.all()
    return render(request, 'tasks/list_ids_user.html', {'tasks': tasks})

def list_resolved_user(request):
    tasks = PendingTask.objects.filter(completed=True)
    return render(request, 'tasks/list_resolved_user.html', {'tasks': tasks})

def list_unresolved_user(request):
    tasks = PendingTask.objects.filter(completed=False)
    return render(request, 'tasks/list_unresolved_user.html', {'tasks': tasks})

class PendingTaskCreateView(CreateView):
    model = PendingTask
    fields = ['user_id', 'title', 'completed']
    template_name = 'tasks/pendingtask_form.html'
    success_url = reverse_lazy('list_ids')

class PendingTaskUpdateView(UpdateView):
    model = PendingTask
    fields = ['user_id', 'title', 'completed']
    template_name = 'tasks/pendingtask_form.html'
    success_url = reverse_lazy('list_ids')

class PendingTaskDeleteView(DeleteView):
    model = PendingTask
    template_name = 'tasks/pendingtask_confirm_delete.html'
    success_url = reverse_lazy('list_ids')

class PendingTaskListView(ListView):
    model = PendingTask
    template_name = 'tasks/pendingtask_list.html'
    context_object_name = 'object_list'



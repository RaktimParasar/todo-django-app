from django.shortcuts import render, redirect
from django.utils import timezone
from . models import Todo
from django.views import generic
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'todo_app/index.html'
    context_object_name = 'todo_items'

    def get_queryset(self):
        return Todo.objects.all().order_by('-date_added')

def add_todo(request):
    content = request.POST['content']
    current_date_time = timezone.now()
    Todo.objects.create(text=content, date_added=current_date_time)
    return redirect('/')

def delete_item(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('/')

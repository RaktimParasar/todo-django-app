from django.urls import path
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('delete_item/<int:todo_id>', views.delete_item, name='delete_item'),
]

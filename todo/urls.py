from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.home, name='todo-home'),
    path('add-task', views.add_task, name='todo-add-task'),
    path('delete-task/<int:id>', views.delete_task, name='todo-delete-task'),
    path('complete-task/<int:id>', views.complete_task, name='todo-complete-task'),
]

from django.contrib import admin
from django.urls import path
from todo.views import todoView, addTodoView, deleteTodoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', todoView),
    path('addTodoItem/',addTodoView),
    path('deleteTodoItem/<int:i>/', deleteTodoView), 
] 
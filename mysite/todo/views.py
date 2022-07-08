from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import TodoListItem 
from django.http import HttpResponseRedirect 
def index(request):
    return HttpResponse("todo firstpage")

# def todoView(request):
#     return render(request, 'todolist.html')

def todoView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items':all_todo_items}) 

def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todo')

def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todo/')
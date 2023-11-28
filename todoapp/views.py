from django.shortcuts import render, redirect
from .models import Todolist, Item
from .forms import CreateTodoForm

# Create your views here.
def index(request):
    todo = Todolist.objects.all()
    context = {'todo' : todo}
    return render(request, 'todoapp/index.html', context)

def createTodo(request):
    if request.method == 'POST':
        form = CreateTodoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            todo = Todolist(name=name)
            todo.save()
            return redirect("todoList")
    else:
        form = CreateTodoForm()
    return render(request, 'todoapp/create.html', {'form': form})

def updateTodo(request, id):
    t = Todolist.objects.get(id=id)
    form = CreateTodoForm(instance=t)
    if request.method == 'POST':
        t = Todolist.objects.get(id=id)
        form = CreateTodoForm(request.POST, instance=t)
        form.save()
        return redirect('todoList')
    return render(request, 'todoapp/edit.html', {'t': form})

def deleteTodo(request, id):
    if request.method == 'POST':
        t = Todolist.objects.get(id=id)
        t.delete()
        return redirect("todoList")
    return redirect(request, 'todoapp/index.html', {'t': form})
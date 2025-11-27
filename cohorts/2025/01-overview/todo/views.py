from django.shortcuts import render, redirect
from .models import Todo


# Create your views here.
def todo_list(request):
    """
    View to list all todo items.
    """
    todos = Todo.objects.all()
    context = {"todos": todos}
    return render(request, "todo/home.html", context)


def add_todo(request):
    """
    View to add a new todo item.
    """
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Todo.objects.create(title=title)
    return redirect("todo_list")


def toggle_todo(request, todo_id):
    """
    View to toggle the completed status of a todo item.
    """
    if request.method == "POST":
        try:
            todo = Todo.objects.get(id=todo_id)
            todo.completed = not todo.completed
            todo.save()
        except Todo.DoesNotExist:
            pass
    return redirect("todo_list")

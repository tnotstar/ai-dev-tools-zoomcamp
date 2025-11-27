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

from django.shortcuts import render
from .models import Todo


# Create your views here.
def todo_list(request):
    """
    View to list all todo items.
    """
    todos = Todo.objects.all()
    context = {"todos": todos}
    return render(request, "todo/home.html", context)

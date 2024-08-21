from django.shortcuts import render,redirect
from  .models import Todo
from .forms import Todolist
def index(request):
    todo=Todo.objects.all()
    form=Todolist()
    if request.method=='POST':
        form=Todolist(request.POST)
        form.save()
        form=Todolist()
        redirect("/")
    context={
        "todo":todo,
        "form":form
    }
    return render(request,"index.html",context)
def edit(request,id):
    todo=Todo.objects.get(id=id)
    form=Todolist(instance=todo)
    if request.method=='POST':
        form=Todolist(request.POST,instance=todo)
        form.save()
        form=Todolist()
        return redirect("/")
    return render(request,"edit.html",{"form":form})
def delete(request,id):
    todo=Todo.objects.get(id=id)
    if request.method=='POST':
        todo.delete()
        return redirect("/")
    return redirect("/")


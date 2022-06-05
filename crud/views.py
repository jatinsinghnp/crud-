from django.shortcuts import redirect, render
from .models import Task
from .forms import TaskForm

# Create your views here.


def home(request):
    tasks = Task.objects.all()
    return render(
        request,
        "index.html",
        {
            "tasks": tasks,
        },
    )


def create(request):

    if request.method == "POST":
        # name=request.POST.get('name'or None)
        # desc=request.POST.get('desc'or None)
        # task=Task()
        # task.name=name
        # task.desc=desc
        # task.save()
        forms = TaskForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("home-page")

        else:
            return redirect("home-page")

    else:
        forms = TaskForm()
        return render(
            request,
            "create.html",
            {"forms": forms},
        )


def update(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        forms = TaskForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("home-page")

    else:
        forms = TaskForm(instance=task)

        return render(request, "update.html", {"forms": forms})


def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()

    return redirect("home-page")

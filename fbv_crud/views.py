from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from fbv_crud.models import Students
from .forms import StudentForm
from django.views.generic import ListView

# Create your views here.


# listing all students  changed to cbv
# def index(request):
#     student = Students.objects.all()
#     return render(request, "fbv_crud/index.html", {"students": student})
class Index(ListView):
    model = Students
    template_name = "fbv_crud/index.html"
    context_object_name = "students"


# Creating a new Students
def create_students(request):
    form = StudentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Student created successfully")
            return redirect(reverse("index"))
    else:
        form = StudentForm()
    return render(request, "fbv_crud/create_students.html", {"form": form})


# Deleting a Students
def delete(request, pk):
    obj = get_object_or_404(Students, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Student deleted successfully")
        return redirect(reverse("index"))

    return render(request, "fbv_crud/delete.html")


# updating a Students
def update(request, pk):
    obj = get_object_or_404(Students, pk=pk)
    form = StudentForm(request.POST or None, instance=obj)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully")
            return redirect(reverse("index"))
    return render(request, "fbv_crud/update.html", {"form": form})

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Student

def index(request):
    return render(request, "student/index.html")

def student_list(request):
    students = Student.objects.all()
    return render(request, "student/partials/list.html", {"students": students})

def student_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        Student.objects.create(name=name, email=email)
        html = render_to_string("student/partials/list.html", {"students": Student.objects.all()})
        return HttpResponse(html + '<div id="modal"></div>')
    return render(request, "student/partials/form.html")

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.save()
        
        html = render_to_string("student/partials/list.html", {"students": Student.objects.all()})
        return HttpResponse(html + '<div id="modal"></div>')
    return render(request, "student/partials/form.html", {"student": student})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "student/partials/detail.html", {"student": student})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    html = render_to_string("student/partials/list.html", {"students": Student.objects.all()})
    return HttpResponse(html + '<div id="modal"></div>')

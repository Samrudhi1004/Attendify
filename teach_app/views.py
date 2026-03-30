from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Teacher
# Create your views here.

@login_required
def teacher_home(request):
    return render(request, 'teach_app/teacher_home.html')

@login_required
def get_all_teachers(request):
    data = Teacher.objects.all() 
    return render(request,"teach_app/display.html", {"teachers": data})

@login_required
def add_teacher(request):
    if request.method == "POST":
        name = request.POST.get('t_name')
        subject = request.POST.get('subject')
        department = request.POST.get('department')
        
        Teacher.objects.create(
            t_name=name,
            subject=subject,
            department=department
        )

        return redirect('teacher:teacher_home')

    return render(request, 'teach_app/add.html')

@login_required
def display_teacher(request):
    teachers = Teacher.objects.all()   # 👈 DB मधून data

    return render(request, 'teach_app/display.html', {
        'teachers': teachers
    })


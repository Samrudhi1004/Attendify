from stud_app.models import Student
from .models import Attendance
from datetime import date
from django.shortcuts import render, redirect

def attendance_home(request):
    return render(request, 'attendance_app/home.html')

def mark_attendance(request):
    students = Student.objects.all()

    if request.method == "POST":
        today = date.today()

        for s in students:
            status = request.POST.get(f"status_{s.roll}")

            if status:
                Attendance.objects.update_or_create(
                    student=s,
                    date=today,
                    defaults={'status': status}
                )

        return redirect('/attendance/view/')

    return render(request, 'attendance_app/mark.html', {'students': students})

def view_attendance(request):
    data = Attendance.objects.all()
    return render(request, 'attendance_app/display.html', {'data': data})
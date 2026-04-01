
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from .serializer import StudentSerializer


# @api_view(['GET'])
# @permission_classes([AllowAny])  # ✅ Allow unauthenticated access
# def get_all_students(request):
#     students = Student.objects.all()
#     serializer = StudentSerializer(students, many=True)
#     return Response(serializer.data)

@login_required(login_url='login')
def home(request):
    return render(request, 'stud_app/home.html')

@login_required(login_url='login')
def student_home(request):
    return render(request, 'stud_app/student_home.html')  

@login_required(login_url='login')
def get_all_students(request):
    data = Student.objects.all()
    students = []

    for student in data:
        students.append({
            'roll': student.roll,
            'name': student.name,
            'subject': student.subject,
            'marks': student.marks
        })

    return render(request, 'stud_app/display.html', {'students': students})



@login_required
def insert_students(request):
    if request.method == "POST":
        r = int(request.POST.get("roll"))  
        name = request.POST.get("name")
        sbj = request.POST.get("subject")
        mks = float(request.POST.get("marks"))

        obj = Student(
            roll=r,
            name=name,    
            subject=sbj,
            marks=mks
        )
        obj.save()

        return redirect('student:display_student')

    return render(request, "stud_app/add.html")



@login_required()
def update_student(request , pk):
    obj = Student.objects.get(roll=pk)
    
    if request.method == "POST":
        #r = int(request.POST.get("roll"))  
        name = request.POST.get("name")
        sbj = request.POST.get("subject")
        mks = float(request.POST.get("marks"))

        obj.name=name    
        obj.subject=sbj
        obj.marks=mks
        obj.save()
        
        return redirect('student:display_student')
    
    context = {'data':obj }
    return render(request, "stud_app/update.html",context) 

@login_required
def delete_student(request, pk):
    obj = Student.objects.get(roll=pk)
    obj.delete()
    return redirect('student:display_student')
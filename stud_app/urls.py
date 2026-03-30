from django.urls import path
from stud_app import views

app_name = 'student'

urlpatterns = [
    path('', views.student_home, name='student_home'),
    path('home/', views.home, name='home_student'),
    path('students/', views.get_all_students , name='display_student'),
    path('insert-one/', views.insert_students , name='add_student'),
    path('update-one/<int:pk>/', views.update_student , name='update_student'),
    path('delete-one/<int:pk>/', views.delete_student , name='delete_student'),
]
from django.urls import path
from teach_app import views

app_name = 'teacher'

urlpatterns = [
     path('', views.teacher_home, name='teacher_home'),
     path('insert-one/', views.add_teacher, name='add_teacher'),
    path('teachers/', views.display_teacher , name='display_teacher'),

]
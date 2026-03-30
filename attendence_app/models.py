from django.db import models

class Student(models.Model):
    roll = models.IntegerField(primary_key=True)   # 🔥 confirm kara
    s_name = models.CharField(max_length=50)


class Attendance(models.Model):
    student = models.ForeignKey('stud_app.Student', on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=1)   # Present / Absent

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"

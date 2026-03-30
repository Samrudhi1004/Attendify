from django.db import models

class Teacher(models.Model):
    t_name = models.CharField(max_length=60)
    subject = models.CharField(max_length=90)
    department = models.CharField(max_length=100)   # ✅ FIX

    def __str__(self):
        return self.t_name   # ✅ FIX

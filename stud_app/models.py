from django.db import models

class Student(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    subject = models.CharField(max_length=90)
    marks = models.FloatField()

    def __str__(self):
        return self.name

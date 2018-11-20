from django.db import models


class StudentForm(models.Model):
    Gender_Choice = (('M', 'Male'), ('F', 'Female'),)
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=1, choices=Gender_Choice)

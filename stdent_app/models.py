from django.db import models
from lead_app.models import *




class Student(Master):
    name = models.CharField(max_length=50)
    DOB = models.DateField()
    gender = models.CharField(max_length=10)
    enquirysource = models.ForeignKey(Enquery_source, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    pincode = models.CharField(max_length=20)
    year_of_passing = models.PositiveIntegerField()
    qualification_name = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=20)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    branches = models.CharField(max_length=200)


    def __str__(self):
        return self.name

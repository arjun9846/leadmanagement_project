from django.contrib import admin
from .models import Student
from lead_app.admin import *

class StudentAdmin(MasterAdmin):
    list_display = ['name', 'DOB', 'gender', 'enquirysource', 'phone', 'email', 'address', 'pincode',
                    'year_of_passing', 'qualification_name', 'reg_no', 'course_name', 'branches', 'place']
    exclude = ['created_user',]

admin.site.register(Student, StudentAdmin)

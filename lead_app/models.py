from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey


# Create your models here.
class Master(models.Model):
    created_user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    isactive=models.BooleanField(default=True,verbose_name='Active')


class State(Master):
    state_name = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.state_name
    
class District(Master):
    state_name=models.ForeignKey(State,on_delete=models.CASCADE)
    district_name=models.CharField(max_length=900)
    def __str__(self):
        return self.district_name
    
class Qualification(Master):
    highest_qualification=models.CharField(max_length=200)
    def __str__(self):
        return self.highest_qualification


class Enquery_source(Master):
    source=models.CharField(max_length=900)
    def __str__(self):
        return self.source
    

class Follow_up_status(Master):
    Follow_up_status=models.CharField(max_length=200)
    def __str__(self):
        return self.Follow_up_status
    

class Branch(Master):
    branch_name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    pincode=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    state_name=models.ForeignKey(State,on_delete=models.CASCADE)
    street=models.CharField(max_length=200)
    branch_code=models.CharField(max_length=200)
    district_name= ChainedForeignKey(
        District,
        chained_field="state_name",
        chained_model_field="State",
         show_all=False,
        auto_choose=True,
        sort=True,
    )   
    def __str__(self):
        return self.branch_name
    

class Course(Master):
    course_name=models.CharField(max_length=200)
    course_code=models.CharField(max_length=200)
    trainer=models.CharField(max_length=200)
    def __str__(self):
        return self.course_name
    


# class Oneteam_Batch(Master):
#     branch_name = models.ForeignKey(Branch, on_delete=models.CASCADE, limit_choices_to={'isactive':True})
#     course_name = models.ForeignKey(Course, on_delete=models.CASCADE, limit_choices_to={'isactive':True})
#     start_date = models.DateField()
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     start_year = models.PositiveIntegerField(editable=False, null=True)
#     batch_name = models.CharField(max_length=100, unique=True,editable=False)
#     trainer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Trainer", null=True, blank=False,related_name="trainer", limit_choices_to={"is_active":True})
#     batch = models.CharField(max_length=255, blank=True)

#     def save(self, *args, **kwargs):
#         self.batch = f"{self.start_date.strftime('%Y')}{self.course_name}{self.start_date.strftime('%dth %B')}{self.start_time.strftime('%I:%M %p')}{self.end_time.strftime('%I:%M %p')}{self.trainer}"
#         super().save(*args, **kwargs)


from django.utils.text import slugify

class Oneteam_Batch(Master):
    branch_name = models.ForeignKey(Branch, on_delete=models.CASCADE, limit_choices_to={'isactive': True})
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE, limit_choices_to={'isactive': True})
    start_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_year = models.PositiveIntegerField(editable=False, null=True)
    batch_name = models.CharField(max_length=100, unique=True, editable=False)
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Trainer", null=True, blank=False, related_name="trainer", limit_choices_to={"is_active": True})
    batch = models.CharField(max_length=255, blank=True)
    
    def save(self, *args, **kwargs):
        self.batch = self.generate_batch_name()
        super().save(*args, **kwargs)

    def generate_batch_name(self):
        branch_slug = slugify(self.branch_name.branch_name)
        course_slug = slugify(self.course_name.course_name)
        date_str = self.start_date.strftime("%Y%m%d")
        return f"{branch_slug}-{course_slug}-{date_str}"

    def __str__(self):
        return self.batch
from django.contrib import admin
from.models import *
# Register your models here.
class MasterAdmin(admin.ModelAdmin):
    list_display=['created_date','created_user','isactive']
    def save_model(self, request,obj,form,change):
        obj.created_user=request.user
        super().save_model(request, obj, form, change)
    

class StateAdmin(MasterAdmin):
    list_display=['state_name','created_date','isactive']
    exclude=['created_user']
    
    
admin.site.register(State, StateAdmin)

class DistrictAdmin(MasterAdmin):
    list_display=['state_name','created_date','isactive','district_name']
    exclude=['created_user']
    
    
admin.site.register(District, DistrictAdmin)

class QualificationAdmin(MasterAdmin):
    list_display=['highest_qualification']
    exclude=['created_user']
    
    
admin.site.register(Qualification, QualificationAdmin)

class Enquery_sourceAdmin(MasterAdmin):
    list_display=['source']
    exclude=['created_user']
    
    
admin.site.register(Enquery_source, Enquery_sourceAdmin)

class Follow_up_statusAdmin(MasterAdmin):
    list_display=['Follow_up_status']
    exclude=['created_user']
    
    
admin.site.register(Follow_up_status, Follow_up_statusAdmin)

class BranchAdmin(MasterAdmin):
    list_display=['branch_name','address']
    exclude=['created_user']
    
    
admin.site.register(Branch, BranchAdmin)


class CourseAdmin(MasterAdmin):
    list_display=['course_name']
    exclude=['created_user']
    
    
admin.site.register(Course, CourseAdmin)   

class Oneteam_BatchAdmin(MasterAdmin):
    list_display=['batch']
    exclude=['created_user']
    

admin.site.register(Oneteam_Batch,Oneteam_BatchAdmin)  

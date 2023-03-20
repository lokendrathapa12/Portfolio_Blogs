from django.contrib import admin
from .models import ContactModel,Blog_Post,Portfolio_Model
# Register your models here.
@admin.register(ContactModel)
class ContactAdminModel(admin.ModelAdmin):
    list_display = ['id','Fullname','email','Phonenumber','message']

@admin.register(Blog_Post)
class BlogAdminModel(admin.ModelAdmin):
    list_display = ['id','image','title','publishdate','content','detail','user']

@admin.register(Portfolio_Model)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ['id','priject_image','porj_link','porj_name','proj_cat','proj_des','user']

'''@admin.register(Comment_Model)
class CommentAdminModel(admin.ModelAdmin):
    list_display = ['id','date','comments','user','blog']'''
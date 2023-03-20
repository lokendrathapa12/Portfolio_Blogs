from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ContactModel(models.Model):
    Fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    Phonenumber = models.IntegerField()
    message = models.CharField(max_length=1000)

class Blog_Post(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    publishdate = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=1000)
    detail = models.CharField(max_length=1000000)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

'''class Comment_Model(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog_Post,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    comments = models.CharField(max_length=10000)'''
    

class Portfolio_Model(models.Model):
    PROJECT_CATEGORY_CHOICES = (
        ('PYTHON', 'Python'),
        ('DJANGO', 'Django'),
        ('REST API', 'RestApi'),
    )
    priject_image = models.ImageField(upload_to='portfolio/images')
    porj_link = models.URLField()
    porj_name =models.CharField(max_length=100)
    proj_cat = models.CharField(max_length=100,choices=PROJECT_CATEGORY_CHOICES)
    proj_des = models.CharField(max_length=10000,default="")
    user = models.ForeignKey(User,on_delete=models.CASCADE)

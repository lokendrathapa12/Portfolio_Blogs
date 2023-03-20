from django import forms
from .models import ContactModel,Blog_Post,Portfolio_Model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class Contact_Form(forms.ModelForm):
    Fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    Phonenumber = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = ContactModel
        fields = '__all__'



class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        label = {'email':'Email'}
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))

class LoginForm(AuthenticationForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        fields = '__all__'
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

class BlogPostForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control'}))
    detail = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Blog_Post
        fields = ['image','user','title','content','detail']

class ProjectPostForm(forms.ModelForm):
    priject_image = forms.ImageField(label='Project Image')
    porj_link = forms.URLField(label='Project Link', widget= forms.URLInput(attrs={'class':'form-control'}))
    porj_name = forms.CharField(label='Project Name', widget = forms.TextInput(attrs={'class':'form-control'}))
    #proj_cat = forms.ChoiceField(label='Project category', widget = forms.Select(attrs={'class':'form-select'}))
    proj_des = forms.CharField(label='Project Description', widget = forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Portfolio_Model
        fields = ['priject_image','porj_link','porj_name','proj_cat','proj_des']


'''class Comment_Form(forms.ModelForm):
    class Meta:
        model = Comment_Model
        fields = '__all__''
    comments = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))'''
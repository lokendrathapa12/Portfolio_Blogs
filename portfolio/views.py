from django.shortcuts import render
from .forms import Contact_Form,RegistrationForm,LoginForm,BlogPostForm,ProjectPostForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from . models import Blog_Post,Portfolio_Model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def Home_View(request):
    return render(request,'portfolio/index.html')

def About_View(request):
    return render(request, 'portfolio/about.html')

@login_required
def Blog_View(request):
    dt = Blog_Post.objects.all()
    return render(request, 'portfolio/blog.html',{'data':dt})

@login_required
def BlogSingle_view(request, id):
    datas = Blog_Post.objects.get(pk=id)
    return render(request,'portfolio/blogsingle.html', {'data':datas})

'''def commentformview(request):
    if request.user:
        if request.method == 'POST':
            fm = Comment_Form(request.POST,request.FILES)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/blogsinglepage/')
        else:
            fm = Comment_Form
        return render(request,'portfolio/blogsingle.html',{'formm':fm})
    else:
        return HttpResponseRedirect('/login/')'''

'''def commentview(request):
    cmt = Comment_Model.objects.all()
    return render (request, 'portfolio/blogsingle.html',{'cmt':cmt})'''

def Contact_View(request):
    if request.method == "POST":
        fm = Contact_Form(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Thanks For Your Message!!!')
            return HttpResponseRedirect("/")
    else:
        fm = Contact_Form()
    return render (request, 'portfolio/contact.html',{'form':fm})

@login_required
def Portfolio_View(request):
    return render(request, 'portfolio/portfolio.html')
@login_required
def allproject(request):
    project = Portfolio_Model.objects.all()
    return render(request, 'portfolio/allproject.html',{'project':project})

@login_required
def pythonproject(request):
    project = Portfolio_Model.objects.all().filter(proj_cat='PYTHON')
    return render(request, 'portfolio/pythonproject.html',{'project':project})

@login_required
def djangoproject(request):
    project = Portfolio_Model.objects.all().filter(proj_cat='DJANGO')
    return render(request, 'portfolio/djangoproject.html',{'project':project})

@login_required
def restapiproject(request):
    project = Portfolio_Model.objects.all().filter(proj_cat='REST API')
    return render(request, 'portfolio/restapiproject.html',{'project':project})

@login_required
def blogformview(request):
    if request.user.is_staff==True:
        if request.method=='POST':
            fm = BlogPostForm(request.POST,request.FILES)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/blog/')
        else:
            fm= BlogPostForm
        return render (request,'portfolio/blogform.html',{'form':fm}) 
    else:
        return HttpResponseRedirect('/message/')

@login_required
def projectformview(request):
    if request.user.is_staff==True:
        if request.method=='POST':
            fm = ProjectPostForm(request.POST,request.FILES)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/portfolio/')
        else:
            fm= ProjectPostForm
        return render (request,'portfolio/portfolioform.html',{'forms':fm}) 
    else:
        return HttpResponseRedirect('/message/')


@login_required
def messageview(request):
    return render (request,'portfolio/message.html')


def registrationview(request):
    if request.method == 'POST':
        fm= RegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        fm = RegistrationForm
    return render (request, 'portfolio/signin.html',{'form':fm})


def loginview(request):
    if request.method  =='POST':
        fm = LoginForm(request=request, data = request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username = uname, password = upass)
            login(request, user)
            return HttpResponseRedirect('/blog/')
    else:
        fm = LoginForm()
    return render(request, 'portfolio/login.html',{'form':fm})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect('/')
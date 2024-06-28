from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
   path("",views.Home_View,name='homepage'), 
   path("about/", views.About_View,name='aboutpage'),
   path("blog/",views.Blog_View,name='blogpage'),
   path("blogform/",views.blogformview,name='blogformpage'),
   path("message/",views.messageview,name='messagepage'),
   path("contact/",views.Contact_View,name='contactpage'),
   path("portfolio/",views.Portfolio_View,name='portfoliopage'),
   path("portfolioform/",views.projectformview,name='portfolioformpage'),
   path("allproject/",views.allproject,name='allprojectpage'),
   path("pythonproject/",views.pythonproject,name='pythonprojectpage'),
   path("djangoproject/",views.djangoproject,name='djangoprojectpage'),
   path("restapiproject/",views.restapiproject,name='restapiprojectpage'),
   path("blogsingle/<int:id>/", views.BlogSingle_view, name='blogsinglepage'),
   path("signin/", views.registrationview, name='signinpage'),
   path('accounts/login/',views.loginview,name='loginpage'),
   path('logout/',views.logoutview,name='logoutpage'),
   #path("comment/", views.commentview, name='commentpage'),
   #path("commentform/", views.commentformview, name='commentformpage'),
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
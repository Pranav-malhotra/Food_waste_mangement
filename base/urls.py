from django.urls import path, include
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name="register"),
    path('res/', views.r, name="restaurant"),
    path('dep/', views.dep, name="department"),
    path('ngo/', views.ngo, name="NGO"),
    
    path('form', views.my_form,name="form"),
    path('about/',views.about,name='about'),
    
    path('feed/',views.feed,name='feed'),
    path('contact/',views.con,name='contact'),

]

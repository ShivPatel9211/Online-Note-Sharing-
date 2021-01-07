
from django.contrib import admin
from django.urls import path ,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
   
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('userlogin/',views.login1,name='userlogin'),
    path('usercreation/',views.usercreation,name='usercreation'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('adminHome/',views.adminHome,name='adminHome'),
    path('logout/',views.logout1,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('uploadnotes/',views.uploadnotes,name='uploadnotes'),
    path('mynotes/',views.mynotes,name='mynotes'),
    path('deletenote/<int:id>',views.deletenote, name='deletenote'),
    path('updatenotes/<int:id>',views.updatenotes, name='updatenotes'),
    path('admindeletenote/<int:id>',views.admindeletenote, name='admindeletenote'),
    path('userdelete/<int:id>',views.userdelete, name='userdelete'),
    path('allnotes/',views.allnotes, name='allnotes'),
    path('adminallnotes/',views.adminallnotes, name='adminallnotes'),
    path('alluser/',views.alluser, name='alluser'),
    path('pandingnotes/',views.pandingnotes, name='pandingnotes'),
    path('acceptednotes/',views.acceptednotes, name='acceptednotes'),
    path('rejectednotes/',views.rejectednotes, name='rejectednotes'),
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

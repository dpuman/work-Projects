from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.userSignup, name='signup'),
    path('login/', views.userLogin, name='userLogin'),
    path('logout/', views.userLogout, name='userLogout'),
    path('add-post/', views.addPost, name='addPost'),
    path('update-post/<int:id>', views.updatePost, name='updatePost'),
    path('delete-post/<int:id>', views.deletePost, name='deletePost'),
]

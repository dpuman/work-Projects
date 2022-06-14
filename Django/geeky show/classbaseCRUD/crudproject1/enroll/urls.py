from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:id>', views.DeleteStudent.as_view(), name='deleteStudent'),
    path('update/<int:id>/', views.UpdateStudent.as_view(), name='updateStudent'),
]

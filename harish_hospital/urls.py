#app1/urls.py
from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('register/', views.register, name= 'register'),
        path('user_login/', views.user_login, name='user_login'),
        path('patient_dashboard/', views.patient_dashboard, name="patient_dashboard")
        ]
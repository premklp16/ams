#app1/urls.py
from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('about-us', views.about_us, name='about_us'),
        path('register/', views.register, name= 'register'),
        path('login/', views.get_login, name='get_login'),
        path('patient-dashboard/', views.patient_dashboard, name="patient_dashboard")
        ]
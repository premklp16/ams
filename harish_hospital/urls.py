
from django.urls import path
from . import views, admin_views

urlpatterns = [
        path('', views.index, name='index'),
        path('about-us', views.about_us, name='about_us'),
        path('register/', views.register, name= 'register'),
        path('login/', views.get_login, name='get_login'),
        path('patient-dashboard/', views.patient_dashboard, name="patient_dashboard"),



        
        path('admin-dashboard/', admin_views.admin_dashboard, name="admin_dashboard"),
        path('admin-doctors/', admin_views.admin_doctors, name="admin_doctors"),
        path('admin-patients/', admin_views.admin_patients, name="admin_patients"),
        
        ]
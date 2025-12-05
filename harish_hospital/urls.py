from django.urls import path
from . import views, admin_views, doctor_views


urlpatterns = [
        #------------------------------------ PUBLIC --------------------------------------------
         
        path('', views.index, name='index'),
        path('about-us/', views.about_us, name='about_us'),
        path('department/',views.department,name='department'),
        path('health-packages/', views.health_packages, name="health_packages"),
        path("logout-user/", views.logout_user, name="logout_user"),
        
        #------------------------------------ PATIENT -------------------------------------------
        
        path('register/', views.register, name= 'register'),
        path('login/', views.get_login, name='get_login'),
        path('patient-dashboard/', views.patient_dashboard, name="patient_dashboard"),
        path('book-success/<uuid:bookid>/', views.booking_success, name="booking_success"),

        #------------------------------------ DOCTOR --------------------------------------------
        
        path('doctor-login/', doctor_views.doctor_get_login, name='doctor_get_login'),
        path("doctor-dashboard", doctor_views.doctor_dashboard, name="doctor_dashboard"),
        path("doctor-profile", doctor_views.doctor_profile, name="doctor_profile"),
        
        #------------------------------------ ADMIN ---------------------------------------------

        path('admin-login/', admin_views.admin_get_login, name='admin_get_login'),
        path('admin-dashboard/', admin_views.admin_dashboard, name="admin_dashboard"),
        path('admin-doctors/', admin_views.admin_doctors, name="admin_doctors"),
        path('admin-patients/', admin_views.admin_patients, name="admin_patients"),
        path('admin-patient/add/', admin_views.admin_add_doctor, name='admin_add_doctor'),
        path('deactivate-doctor/<uuid:id>/', admin_views.deactivate_doctor, name='deactivate_doctor'),
        
        ]
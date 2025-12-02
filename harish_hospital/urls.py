from django.urls import path
from . import views, admin_views, doctor_views

urlpatterns = [
        path('', views.index, name='index'),
        path('about-us/', views.about_us, name='about_us'),
        path('register/', views.register, name= 'register'),
        path('login/', views.get_login, name='get_login'),
        path('patient-dashboard/', views.patient_dashboard, name="patient_dashboard"),
        path('book-success/<int:bookid>/', views.booking_success, name="booking_success"),
        path("logout-user/", views.logout_user, name="logout_user"),


        path("doctor-dashboard", doctor_views.doctor_dashboard, name="doctor_dashboard"),
        path("doctor-profile", doctor_views.doctor_profile, name="doctor_profile"),


        
        path('admin-dashboard/', admin_views.admin_dashboard, name="admin_dashboard"),
        path('admin-doctors/', admin_views.admin_doctors, name="admin_doctors"),
        path('admin-patients/', admin_views.admin_patients, name="admin_patients"),
        path('admin-patient/add/', admin_views.admin_add_doctor, name='admin_add_doctor'),
        # path('post-donation-detail/edit/<uuid:pk>/', views.create_or_edit_post_donation_detail, name='edit_post_donation_detail'),
        
        ]
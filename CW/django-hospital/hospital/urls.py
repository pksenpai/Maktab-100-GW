from django.contrib import admin
from django.urls import path
from .views import DoctorSignUpView, PatientSignUpView, home

app_name = 'hospital'
urlpatterns = [
    path('', home),
    # path('doctor', DoctorListView.as_view(), name='doctor'),
    path('signup/doctor', DoctorSignUpView.as_view(), name='d_signup'),
    path('signup/patient', PatientSignUpView.as_view(), name='p_signup'),
]

from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'hospital'
urlpatterns = [
    path('', home , name='home'),
    path('signup/doctor', DoctorSignUpView.as_view(), name='d_signup'),
    path('signup/patient', PatientSignUpView.as_view(), name='p_signup'),
    path('ph/', PatientHistoryView.as_view(), name='ph'),
    path('visit/', AddVisit.as_view(), name='addvisit'),
]

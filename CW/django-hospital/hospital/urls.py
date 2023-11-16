from django.contrib import admin
from django.urls import path
from .views import DoctorListView, DoctorSignUpView


urlpatterns = [
    path('doctor', DoctorListView.as_view()),
    path('doctor/signup', DoctorSignUpView.as_view()),
]

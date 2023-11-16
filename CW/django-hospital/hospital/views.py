from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, CreateView
# CBV, FBV

# def show_doctors(request):
#     doctors = Doctor.objects.select_related("specialization")
    
#     return render(request, "doctor_list.html", {'doctors': doctors})

class DoctorListView(ListView):
    queryset            = Doctor.objects.select_related("specialization")
    template_name       = "doctor_list.html"
    context_object_name = "doc"
    # template_name_suffix

class DoctorSignUpView(CreateView):
    model          = Doctor
    template_name  = "doctor_form.html"
    fields         = "__all__"
    
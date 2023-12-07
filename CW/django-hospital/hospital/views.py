from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, CreateView, View


def home(request):
    template = "base.html"
    return render(request, template, {})


# class DoctorListView(ListView):
#     queryset            = User.objects.filter(role='Doctor')
#     template_name       = "doctor_list.html"
#     context_object_name = "doc"


# class SignUpMixin(CreateView):
#     initial = {"key": "value"}
    
class DoctorSignUpView(CreateView): # name%%%
    template_name = "doctor_signup_form.html"
    model = CustomUser
    fields = ['national_code' ,'password']
    success_url = reverse_lazy('hospital:home')
   

    def form_valid(self, form ):
        form.instance.role = 'D'
        return super().form_valid(form)
    
class PatientSignUpView(CreateView): # name%%%
    template_name = "patient_signup_form.html"
    model = CustomUser
    fields = ['national_code' ,'password']
    success_url = reverse_lazy('hospital:home')
   

    def form_valid(self, form ):
        form.instance.role = 'P'
        return super().form_valid(form)


        # return render(request, self.template_name, {"form": form})
    
# class PatientSignUpView(): # name%%%
#     # form = PForm
#     template_name = "patient_signup_form.html"

# class UserLogin()

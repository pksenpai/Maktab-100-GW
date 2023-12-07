from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import ListView, CreateView, View


def home(request):
    template = "base.html"
    return render(request, template, {})


# class DoctorListView(ListView):
#     queryset            = User.objects.filter(role='Doctor')
#     template_name       = "doctor_list.html"
#     context_object_name = "doc"


class SignUpMixin(View):
    form_class = MyForm
    initial = {"key": "value"}
    
class DoctorSignUpView(SignUpMixin): # name%%%
    template_name = "form_template.html"


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect("/success/")

        return render(request, self.template_name, {"form": form})
    
class PatientSignUpView(SignUpMixin): # name%%%
    # form = PForm
    template_name = "patient_signup_form.html"

# class UserLogin()

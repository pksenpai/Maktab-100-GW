from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, CreateView, View
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


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


class PatientHistoryView(ListView, PermissionRequiredMixin, LoginRequiredMixin):
    model = PatientHistory
    template_name = 'patient_history.html'
    # permission_required = ''
    context_object_name = "phs"
    
    def get_queryset(self):
        own_doctor = self.model.objects.filter(visit__user__national_code=self.request.user.national_code)
        print(own_doctor)
        
        return super().get_queryset()

class AddVisit(CreateView, PermissionRequiredMixin, LoginRequiredMixin):
    model = Visit
    template_name = 'visit.html'
    permission_required = 'hospital.add_visit'
    fields = ['time' ,'reason']
    success_url = reverse_lazy('hospital:home')
    
    def form_valid(self, form):
        form.instance.user.username = self.request.user.username
        form.instance.user.password = self.request.user.password
        form.instance.user.role = self.request.user.role
        form.instance.user.national_code = self.request.user.national_code
        
        return super().form_valid(form)
    
    def get_queryset(self):
        own_doctor = self.model.objects.filter(visit__user__national_code=self.request.user.national_code)
        print(own_doctor)
        
        return super().get_queryset()

# @method_decorator(csrf_exempt, name='dispatch')
# class PostListView(ListView):
#     model = Post
    # permission_required = ('posts.view_post', 'posts.ban_user')
    # permission_denid = 'posts.ban_user'
    # permission_denied_message = 'from permission_denied_message attr no permission'
    # def handle_no_permission(self):
    #     if self.raise_exception or self.request.user.is_authenticated:
    #         return HttpResponse('you have not permission')
    # raise PermissionDenied('you have not permission')
    
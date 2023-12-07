from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import *

class CustomUserAdmin(UserAdmin):
    pass
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    # modeCustomUserl = 
    # list_display = [
    # 'email',
    # 'username',
    # 'is_staff',
    #                 ]
    # fieldsets = UserAdmin.fieldsets + \
    # ((None, {"fields": ('age', 'about', 'photo')}),)
    # add_fieldsets = UserAdmin.add_fieldsets + \
    # ((None, {"fields": ('age', 'about', 'photo')}),)

admin.site.register(PatientBill)
admin.site.register(PatientHistory)
admin.site.register(Visit)
admin.site.register(HealthInsurance)
admin.site.register(Specialization)
admin.site.register(CustomUser)



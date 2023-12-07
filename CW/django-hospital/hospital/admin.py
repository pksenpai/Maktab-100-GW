from django.contrib import admin
from .models import *

admin.site.register(PatientBill)
admin.site.register(PatientHistory)
admin.site.register(Visit)
admin.site.register(HealthInsurance)
admin.site.register(Specialization)
admin.site.register(User)


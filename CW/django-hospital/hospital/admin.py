from django.contrib import admin
from .models import Doctor, Patient, PatientBill, PatientHistory, Visit, HealthInsurance, Specialization

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(PatientBill)
admin.site.register(PatientHistory)
admin.site.register(Visit)
admin.site.register(HealthInsurance)
admin.site.register(Specialization)

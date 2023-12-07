from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser


PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

ROLES = [
    ("D", "Doctor"),
    ("P", "Patient"),
]


class UserInfo(models.Model):
    gender = models.CharField(max_length=10)
    birth_date = models.DateField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    health_insurance = models.ForeignKey(
        "HealthInsurance", on_delete=models.SET_NULL, related_name="patient", null=True
    )
    verified = models.BooleanField(default=False)
    specialization = models.ForeignKey(
        "Specialization", on_delete=models.CASCADE, related_name="doctor"
    )
    medical_code = models.CharField(max_length=20)


class CustomUser(AbstractUser):
    national_code = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=1, choices=ROLES)
    user_info = models.OneToOneField(UserInfo, on_delete=models.SET_NULL, blank=True, null=True)


class Specialization(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class HealthInsurance(models.Model):
    company_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    payment_discount_percentage = models.DecimalField(
        max_digits=3, decimal_places=0, validators=PERCENTAGE_VALIDATOR
    )

    def __str__(self):
        return f"{self.company_name}"


class PatientHistory(models.Model):
    diagnosis = models.TextField()
    prescription = models.TextField()


class Visit(models.Model):
    User = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user")
    time = models.DateTimeField()
    reason = models.CharField(max_length=200)
    patient_history = models.ForeignKey(
        PatientHistory, on_delete=models.CASCADE, related_name="patient_history"
    )


class PatientBill(models.Model):
    visit = models.OneToOneField(
        Visit, on_delete=models.CASCADE, related_name="patient_bill"
    )
    total_cost = models.BigIntegerField()

    def patient_payable(self):
        payable = self.total_cost - (
            self.total_cost - (self.visit.patient.payment_discount_percentage / 100)
        )
        return payable

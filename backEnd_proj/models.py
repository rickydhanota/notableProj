from django.db import models

# Create your models here.
class Doctor(models.Model):
    firstName = models.CharField(max_length = 255)
    lastName = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

class Appointment(models.Model):
    patient_firstName = models.CharField(max_length = 255)
    patient_lastName = models.CharField(max_length = 255)
    appointmentTime = models.DateTimeField()
    kind = models.CharField(max_length = 255)
    doctor = models.ForeignKey(Doctor, related_name = "appointments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

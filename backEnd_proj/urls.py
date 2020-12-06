from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("getAllDoctors/", views.getAllDoctors, name = "getAllDoctors"),
    path("getDoctorsAppointments/<int:doctor_id>/<str:date>/", views.getDoctorAppointments),
    path("deleteDoctorAppointment/<int:appointment_id>/", views.deleteDoctorAppointment),
    path("newAppointment/", views.newAppointment),
]
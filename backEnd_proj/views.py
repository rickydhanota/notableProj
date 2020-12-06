from django.shortcuts import render, redirect, HttpResponse
from django.core import serializers
from .models import *
import json
import datetime

# For the take-home, we ask you to implement a web backend that serves up some data with a couple of GET, POST, and DELETE requests (data can be in a DB, or hard-coded, whatever you prefer) It’s based on an actual problem we solved here and meant to be representative of the kind of work we’d do together day to day week to week.  


def home(request):
    return render(request, "index.html")

def getAllDoctors(request):
    #This is a GET request
    if request.method == "GET":
        all_doctors = Doctor.objects.all()
        all_doctors_json = serializers.serialize('json', all_doctors)
        return HttpResponse(all_doctors_json, content_type='application/json')

def getDoctorAppointments(request, doctor_id, date):
    #This is a GET request
    if request.method == "GET":
        appointmentDate = datetime.datetime.strptime(date, "%Y-%m-%d")
        doctor = Doctor.objects.get(id = doctor_id)
        get_doctor_appointments = doctor.appointments.filter(appointmentTime__year=appointmentDate.year, appointmentTime__month=appointmentDate.month, appointmentTime__day = appointmentDate.day)
        get_doctor_appointments_json = serializers.serialize('json', get_doctor_appointments)
        return HttpResponse(get_doctor_appointments_json, content_type='application/json')

def deleteDoctorAppointment(request, appointment_id):
    if request.method == "POST":
        appointment = Appointment.objects.get(id = appointment_id)
        appointment.delete()
        print("Appointment Deleted")
        return redirect("/getAllDoctors/")
    else:
        return HttpResponse("Needs to be a POST request")

def newAppointment(request):
    if request.method == "GET":
        return render(request, "createAppointment.html")
    else:
        appointment = datetime.datetime.strptime(request.POST["appointmentDate"], "%Y-%m-%dT%H:%M")
        if appointment.minute%15 != 0:
            return HttpResponse("Need time to be in 15 minute intervals")
        else:
            doctor = Doctor.objects.get(id = request.POST["doctor"])
            max3appointment = doctor.appointments.filter(appointmentTime = appointment)
            print(max3appointment)
            if len(max3appointment) < 4:
                newAppointment = Appointment.objects.create(patient_firstName = request.POST["patient_firstName"], patient_lastName = request.POST["patient_lastName"], appointmentTime = appointment, kind = request.POST["kind"], doctor = doctor)
                return HttpResponse("Your Appointment Has Been Created")
            else:
                return HttpResponse("Too Many Appoinemnts")
    






# Create your views here
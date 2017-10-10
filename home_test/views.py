from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

from .forms import SignInForm, PatientForm, AppoimentForm, TreatmentForm, BillForm
from .models import UserProfile, Treatment, Appoiment, Bill, Patient

from datetime import date
# doctor
def dotodaypatient(request):
    return render(request, "doctor/today_patient/today_patient.html",{})

def dotodaypatientdetails(request):
    return render(request, "doctor/today_patient/today_patient_details.html",{})

def dochangepassword(request):
    return render(request, "doctor/common/change_password.html",{})

# receptionist
def retodaybooking(request):
    today_booking = Appoiment.objects.filter(date=date.today())
    today_treatment = Treatment.objects.filter(created_at=date.today())
    return render(request, "receptionist/today_booking/today_booking.html",{ 'today_booking': today_booking, 'today_treatment': today_treatment})

def readdappoinment(request):
    form = AppoimentForm()
    if request.method == 'POST':
        form = AppoimentForm(request.POST)
        if form.is_valid():
            appoiment = form.save()
            return HttpResponseRedirect("/home_test/retodaybooking/")
    return render(request, "receptionist/today_booking/add_appoinment.html", { 'form': form})

def readdtreatment(request):
    form = TreatmentForm()
    if request.method == 'POST':
        form = TreatmentForm(request.POST)
        if form.is_valid():
            treatment = form.save()
            return HttpResponseRedirect("/home_test/retodaybooking/")
    return render(request, "receptionist/today_booking/add_treatment.html", { 'form': form})

def doctorlist(request):
    doctors = UserProfile.objects.filter(user_type='DOCTOR')
    return render(request, "receptionist/doctor_list/doctor_list.html",{ 'doctors': doctors})

def patientlist(request):
    patients = Patient.objects.all()
    print(patients)
    return render(request, "receptionist/patient_list/patient_list.html",{ 'patients': patients})

def rebill(request):
    bills = Bill.objects.filter(date=date.today())
    return render(request, "receptionist/bill/bill.html",{ 'bills': bills})

def readdbill(request):
    form = BillForm()
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            bill = form.save()
            return HttpResponseRedirect("/home_test/rebill/")
    return render(request, "receptionist/bill/bill_add.html",{ 'form': form})	

def rechangepassword(request):
    return render(request, "receptionist/common/change_password.html",{})

def readdpatient(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            return HttpResponseRedirect("/home_test/retodaybooking/")
    return render(request, "receptionist/today_booking/add_patient.html", { 'form': form})
	
# patient	
def patienthome(request):
    return render(request, "patient/home/home.html",{})
def padetails(request):
    return render(request, "patient/home/details.html",{})	
def pachangepassword(request):
    return render(request, "patient/common/change_password.html",{})
	
# frontpage  
class HomeView(View):
    def get(self, request,*args, **kwargs):
        return render(request, "frontpage/index.html")	

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = 	authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            userprofile = UserProfile.objects.get(user=user)
            if userprofile.user_type == 'RECEPTIONIST':
                return HttpResponseRedirect('/home_test/retodaybooking/')
            elif user.UserProfile.user_type == 'DOCTOR':
                return HttpResponseRedirect('/home_test/dotodaypatient/')
            else:
                return HttpResponseRedirect('/home_test/patienthome')
    return render(request, 'frontpage/index.html')

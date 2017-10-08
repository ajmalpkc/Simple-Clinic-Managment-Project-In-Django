from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

from .forms import SignInForm

# doctor
def dotodaypatient(request):
    return render(request, "doctor/today_patient/today_patient.html",{})
def dotodaypatientdetails(request):
    return render(request, "doctor/today_patient/today_patient_details.html",{})
def dochangepassword(request):
    return render(request, "doctor/common/change_password.html",{})

# receptionist
def retodaybooking(request):
    return render(request, "receptionist/today_booking/today_booking.html",{})	
def doctorlist(request):
    return render(request, "receptionist/doctor_list/doctor_list.html",{})
def redepartment(request):
    return render(request, "receptionist/department/department.html",{})
def readddepartment(request):
    return render(request, "receptionist/department/department_add.html",{})	
def rechangepassword(request):
    return render(request, "receptionist/common/change_password.html",{})
	
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
        receptionist=Group.objects.filter(name='receptionist')
        doctor=Group.objects.filter(name='doctor')
        user = 	authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name__in=['receptionist']):
                return HttpResponseRedirect('/home_test/retodaybooking/')
            elif user.groups.filter(name__in=['doctor']):
                return HttpResponseRedirect('/home_test/dotodaypatient/')
            else:
                return HttpResponseRedirect('/home_test/patienthome')
    return render(request, 'frontpage/index.html')

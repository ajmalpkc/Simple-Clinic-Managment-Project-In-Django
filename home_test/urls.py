from django.conf.urls import url
from django.contrib import admin
from .views import (

  # doctor
	dotodaypatient,
	dotodaypatientdetails,
	dochangepassword,
	
  # receptionist
    retodaybooking,
	doctorlist,
	redepartment,
	readddepartment,
	rechangepassword,
	readdpatient,
	
  # patient
    patienthome,
	padetails,
	pachangepassword
	)
	
	

urlpatterns = [

    # doctor
	 url(r'^dotodaypatient/$', dotodaypatient, name='dotodaypatient'),
	 url(r'^dotodaypatientdetails/$', dotodaypatientdetails, name='dotodaypatientdetails'),
	 url(r'^dochangepassword/$', dochangepassword, name='dochangepassword'),
	 
	# receptionist
	 url(r'^retodaybooking/$', retodaybooking, name='retodaybooking'),
	 url(r'^doctorlist/$', doctorlist, name='doctorlist'),
	 url(r'^redepartment/$', redepartment, name='redepartment'),
	 url(r'^readddepartment/$', readddepartment, name='readddepartment'),
	 url(r'^rechangepassword/$', rechangepassword, name='rechangepassword'),
	 url(r'^addpatient/$', readdpatient, name="addpatient"),
	 
	 # patient
	 url(r'^patienthome/$', patienthome, name='patienthome'),
	 url(r'^padetails/$', padetails, name='padetails'),
	 url(r'^pachangepassword/$', pachangepassword, name='pachangepassword'),
	 
]


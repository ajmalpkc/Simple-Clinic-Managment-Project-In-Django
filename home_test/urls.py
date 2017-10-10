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
	rebill,
	readdbill,
	rechangepassword,
	readdpatient,
	patientlist,
	readdappoinment,
	readdtreatment,
	
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
	 url(r'^rebill/$', rebill, name='rebill'),
	 url(r'^readdbill/$', readdbill, name='readdbill'),
	 url(r'^rechangepassword/$', rechangepassword, name='rechangepassword'),
	 url(r'^addpatient/$', readdpatient, name="addpatient"),
	 url(r'^patientlist/$', patientlist, name="patientlist"),
	 url(r'^addappoinment/$', readdappoinment, name="addappoinment"),
	 url(r'^addtreatment/$', readdtreatment, name="addtreatment"),
	 
	 # patient
	 url(r'^patienthome/$', patienthome, name='patienthome'),
	 url(r'^padetails/$', padetails, name='padetails'),
	 url(r'^pachangepassword/$', pachangepassword, name='pachangepassword'),
	 
]


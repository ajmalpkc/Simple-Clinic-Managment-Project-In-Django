from django.db import models
from django.contrib.auth.models import User

USER_TYPE = (('DOCTOR', 'DOCTOR'), ('RECEPTIONIST', 'RECEPTIONIST'),)
USER_SPECIALISED = (('EMPLANT', 'EMPLANT'), ('ORTHO', 'ORTHO'))
USER_GENDER = (('MALE', 'MALE'), ('FEMALE', 'FEMALE'))
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	user_type = models.CharField(max_length=15, choices=USER_TYPE, default='PATIENT')
	user_addr = models.CharField(max_length=155, null=True )
	user_mobile = models.IntegerField(null=True )
	user_hire_date = models.DateField(blank=True, null=True)
	user_dob = models.DateField(blank=True, null=True)
	user_specialised = models.CharField(max_length=15, choices=USER_SPECIALISED, blank=True, null=True)
	user_sex = models.CharField(max_length=10, choices=USER_GENDER, default='MALE')
	user_qualification = models.CharField(max_length=100, blank=True, null=True)
	user_bloodgroup = models.CharField(max_length=10, blank=True, null=True)
	def __str__(self):
		return str(self.user.username)

class Patient(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100, blank=True, null=True)
	phone = models.CharField(max_length=20, blank=True, null=True)
	address = models.CharField(max_length=200, blank=True, null=True)
	bloodgroup = models.CharField(max_length=10, blank=True, null=True)
	sex = models.CharField(max_length=10, choices=USER_GENDER, default='MALE')
	age = models.IntegerField(blank=True, null=True)
	created_at = models.DateField(auto_now_add=True, blank=True, null=True)
	updated_at = models.DateField(auto_now=True, blank=True, null=True)
	def __str__(self):
		return str(self.name)

class Treatment(models.Model):
	patient = models.ForeignKey(Patient)
	doctor = models.ForeignKey(User, related_name='treat_doctor')
	title = models.CharField(max_length=50)
	token = models.IntegerField()
	description = models.CharField(max_length=100, blank=True, null=True)
	dental_position = models.CharField(max_length=50, blank=True, null=True)
	dental_test = models.CharField(max_length=100, blank=True, null=True)
	created_at = models.DateField(auto_now_add=True, blank=True, null=True)
	updated_at = models.DateField(auto_now=True, blank=True, null=True)
	def __str__(self):
		return str(self.patient)

class Appoiment(models.Model):
	patient = models.ForeignKey(Patient)
	doctor = models.ForeignKey(User, related_name='app_doctor')
	token = models.IntegerField()
	date = models.DateField(blank=True, null=True)
	time = models.TimeField(null=True, blank=True)
	created_at = models.DateField(auto_now_add=True, blank=True, null=True)
	updated_at = models.DateField(auto_now=True, blank=True, null=True)

	def __str__(self):
		return str(self.patient.username)

	class Meta:
		ordering = ('date',)

class Bill(models.Model):
	date = models.DateField(auto_now=True)
	patient = models.ForeignKey(Patient)
	doctor = models.ForeignKey(User, related_name='bill_doctor')
	treatment = models.ForeignKey(Treatment)
	amount = models.IntegerField()
	def __str__(self):
		return str(self.patient)
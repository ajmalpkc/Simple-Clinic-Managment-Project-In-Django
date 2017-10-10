from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Patient, Appoiment, Treatment, Bill

class SignInForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password',)


class PatientForm(ModelForm):
	class Meta:
		model = Patient
		fields = ('name', 'email', 'phone', 'address', 'bloodgroup', 'sex', 'age')

class AppoimentForm(ModelForm):
	class Meta:
		model = Appoiment
		fields = ('patient', 'doctor', 'token', 'date', 'time')

class TreatmentForm(ModelForm):
	class Meta:
		model = Treatment
		fields = ('patient', 'doctor', 'title', 'token', 'description', 'dental_position', 'dental_test')

class BillForm(ModelForm):
	class Meta:
		model = Bill
		fields = ( 'patient', 'doctor', 'treatment', 'amount')

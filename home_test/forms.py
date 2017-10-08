from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Patient

class SignInForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password',)


class PatientForm(ModelForm):
	class Meta:
		model = Patient
		fields = ('name', 'email', 'phone', 'address', 'bloodgroup', 'sex', 'age')
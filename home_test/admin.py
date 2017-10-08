from django.contrib import admin
from .models import UserProfile, Treatment, Appoiment, Bill, Patient
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Treatment)
admin.site.register(Appoiment)
admin.site.register(Bill)
admin.site.register(Patient)
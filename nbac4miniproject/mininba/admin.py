from django.contrib import admin
from .models import AdmissionDetails, Students

# Register models
admin.site.register(AdmissionDetails)
admin.site.register(Students)

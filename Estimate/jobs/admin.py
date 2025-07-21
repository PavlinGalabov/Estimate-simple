from django.contrib import admin
from .models import Client, Job, MasterOperation, JobOperation

admin.site.register(Client)
admin.site.register(Job)
admin.site.register(MasterOperation)
admin.site.register(JobOperation)

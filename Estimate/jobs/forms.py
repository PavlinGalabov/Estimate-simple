from django import forms
from django.forms import inlineformset_factory
from .models import Job, JobOperation

JobOperationFormSet = inlineformset_factory(
    Job,
    JobOperation,
    fields=['master_operation', 'sequence'],
    extra=1,
    can_delete=True
)

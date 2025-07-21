from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Job
from django.shortcuts import redirect, render
from .forms import JobOperationFormSet

class JobListView(ListView):
    model = Job
    template_name = 'jobs/job_list.html'

class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/job_detail.html'

class JobCreateView(CreateView):
    model = Job
    fields = '__all__'
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('jobs:job-list')

class JobUpdateView(UpdateView):
    model = Job
    fields = '__all__'
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('jobs:job-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['operation_formset'] = JobOperationFormSet(self.request.POST, instance=self.object)
        else:
            context['operation_formset'] = JobOperationFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        operation_formset = context['operation_formset']
        if form.is_valid() and operation_formset.is_valid():
            self.object = form.save()
            operation_formset.instance = self.object
            operation_formset.save()
            return redirect(self.success_url)
        return self.form_invalid(form)

class JobDeleteView(DeleteView):
    model = Job
    template_name = 'jobs/job_confirm_delete.html'
    success_url = reverse_lazy('jobs:job-list')

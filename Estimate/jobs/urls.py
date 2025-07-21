from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.JobListView.as_view(), name='job-list'),
    path('job/create/', views.JobCreateView.as_view(), name='job-create'),
    path('job/<int:pk>/', views.JobDetailView.as_view(), name='job-detail'),
    path('job/<int:pk>/edit/', views.JobUpdateView.as_view(), name='job-update'),
    path('job/<int:pk>/delete/', views.JobDeleteView.as_view(), name='job-delete'),
]

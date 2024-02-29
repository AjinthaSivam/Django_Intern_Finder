from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('job-listing/', views.job_listing, name='job-listing'),
   path('job-details/<int:pk>/', views.job_details, name='job-details'),
   path('about-us/', views.about_us,name='about-us'),
   path('contact-us/', views.contact_us,name='contact-us')
]
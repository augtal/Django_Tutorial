from django.urls import path

from . import views

urlpatterns = [
    path('meetups/', views.index, name='meetups-all'), #our domain.com/meetups
    path('meetups/<slug:meetup_slug>/success/', views.confirm_registration, name='meetups-registration-success'),
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetups-details'), #our domain.com/meetups/<dynamic-path-segment>a-first-meetup
]

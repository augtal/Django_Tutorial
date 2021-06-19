from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='meetups-all'), #our domain.com/meetups
    path('<slug:meetup_slug>/success/', views.confirm_registration, name='meetups-registration-success'),
    path('<slug:meetup_slug>', views.meetup_details, name='meetups-details'), #our domain.com/meetups/<dynamic-path-segment>a-first-meetup
]

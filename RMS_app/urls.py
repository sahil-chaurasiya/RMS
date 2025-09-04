from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='home'),           # default page
    path('analytics.html', views.analytics, name='analytics'),
    path('battery.html', views.battery, name='battery'),
]

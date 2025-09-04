from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='home'),           # default page
    path('analytics', views.analytics, name='analytics'),
    path('battery', views.battery, name='battery'),
    path('admin', views.admin, name='admin'),
    path('energy', views.energy, name='energy'),
    path('grid_billing', views.grid_billing, name='grid_billing'),
    path('login', views.login, name='login'),
    path('maps', views.maps, name='maps'),
    path('reports', views.reports, name='reports'),

]

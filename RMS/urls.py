from django.contrib import admin
from django.urls import path
from RMS_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('analytics/', views.analytics, name='analytics'),
    path('battery/', views.battery, name='battery'),
    path('useradmin/', views.useradmin, name='useradmin'),
    path('energy/', views.energy, name='energy'),
    path('grid_billing/', views.grid_billing, name='grid_billing'),
    path('/login', views.login, name='login'),
    path('maps/', views.maps, name='maps'),
    path('reports/', views.reports, name='reports'),
]
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
   # return HttpResponse("this is homepage")

def analytics(request):
    return render(request, "analytics.html")

def battery(request):
    return render(request, "battery.html")

def useradmin(request):
    return render(request, "useradmin.html")

def energy(request):
    return render(request, "energy.html")

def grid_billing(request):
    return render(request, "grid_billing.html")

def login(request):
    return render(request, "login.html")

def maps(request):
    return render(request, "maps.html")

def reports(request):
    return render(request, "reports.html")
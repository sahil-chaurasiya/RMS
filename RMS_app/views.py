from django.shortcuts import render

def demo(request):
    return render(request, "demo.html")

def analytics(request):
    return render(request, "analytics.html")

def battery(request):
    return render(request, "battery.html")

def admin(request):
    return render(request, "admin.html")

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









from django.shortcuts import render, redirect



# Create your views here.
def activity(request):
    return render(request, 'dashboard/activity.html')

def contact(request):
    return render(request, 'dashboard/contact.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def history(request):
    return render(request, 'dashboard/history.html')

def settings(request):
    return render(request, 'dashboard/settings.html')

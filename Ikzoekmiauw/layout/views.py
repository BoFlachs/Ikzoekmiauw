from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def privacy(request):
    return render(request, "privacy.html")

def ditjes(request):
    return render(request, "ditjes.html")
from django.shortcuts import render

# Create your views here.
def katalogus(request):
    return render(request, 'katalogus.html')
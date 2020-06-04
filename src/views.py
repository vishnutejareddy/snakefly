from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {'body': True})

def about(request):
    return render(request, 'index.html', {'about': True})

def members(request):
    return render(request, 'index.html', {'members': True})

def events(request):
    return render(request, 'index.html', {'events': True})

def read_more(request):
    return render(request, 'index.html', {'read_more': True})

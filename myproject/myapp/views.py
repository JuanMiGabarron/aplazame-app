from django.shortcuts import render


# index view
def index(request):
    return render(request, 'myapp/index.html')

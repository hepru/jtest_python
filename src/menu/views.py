from django.shortcuts import render

# Create your views here.

def getMenu(request, name):
    context = {
        'name': name
    }
    return render(request, 'menu/home.html', context)

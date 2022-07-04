from django.shortcuts import render
from .forms import UserForm
# Create your views here.


def NavView(request):
    return render(request, 'nav.html')


def HomeView(request):
    return render(request,'home.html')


def RegisterView(request):
    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid():
            fm.save()
            print('Registation Successfully....')
        else:
            print('Registation Failed....')
            
    else:
        print('Request method not POST....')
            
    fm = UserForm()
    return render(request, 'register.html', {'form': fm})
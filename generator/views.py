from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    # return HttpResponse("Welcome to New Learning Shashank !!")
    return render(request,'generator/home.html')

def password(request):

    length = int(request.GET.get('length',12))
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special character'):
        characters.extend(list('!@#$^&*()_+{}><~,'))
    if request.GET.get('number'):
        characters.extend(list('0123456789'))
    
    thepassword = ''

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password' : thepassword})

def about(request):
    return  render(request,'generator/about.html')
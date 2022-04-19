from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator\home.html',{'password':'sean123'})

def about(request):
    return render(request,'generator\open.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend([x.upper() for x in characters])
    if request.GET.get('Special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend([str(x) for x in range(0,10)])
    #return HttpResponse(characters)
    length = int(request.GET.get('length',12))
    passwd = ''

    for x in range(length):
        passwd += random.choice(characters)
    return render(request,'generator\password.html',{'password':passwd})

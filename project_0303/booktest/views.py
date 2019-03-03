from django.shortcuts import render,redirect
from booktest.models import BookInfo
from django.http import HttpResponse


# Create your views here.
def myfilter(request):
    context={'list':BookInfo.objects.all()}
    return render(request,'booktest/myfilter.html',context)


def block(request):
    return render(request,'booktest/child.html')


def login(request):
    '''login - page'''
    return render(request,'booktest/login.html')


def logincheck(request):
    '''login check - page'''
    username = request.POST.get('username')
    password = request.POST.get('password')
    if (username=="admin" and password=="123"):
        return render(request,'booktest/change_pwd.html')
    else:
        return redirect('/login')

def changepwd(request):
    return render(request,'booktest/changepwd.html')


def changeover(request):
    password = request.POST.get('password')
    return render(request,'booktest/changeover.html',{"pwd":password})


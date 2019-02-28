from django.shortcuts import render,redirect
from booktest.models import *
from datetime import date
# Create your views here.
def index(request):
    book = BookInfo.objects.all();
    return render(request,'booktest/index.html',{'book':book})

def create(request):
    b = BookInfo()
    b.btitle = "追风筝的人"
    b.bpub_date=date(2016,12,3)
    b.save()
    return redirect('/index')

def delete(request,bid):
    book = BookInfo.objects.get(id=bid)
    book.delete()
    # 转向到首页
    return redirect('/index')

def area(request):
    area = AreaInfo.objects.get(pk=440100)
    return render(request, 'booktest/area.html', {'area': area})
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from booktest.models import BookInfo,HeroInfo

def index(request):
    #return HttpResponse('index,index,hello index!')
    #temp=loader.get_template('booktest/index.html')
    #context = RequestContext(request,{})
    #res = temp.render(context)
    #return HttpResponse(res)
    return render(request,"booktest/index.html",{"content":"hello","lists":list(range(1,10))})

def login(request):
    return HttpResponse('login,login,hello login!')

def show_book(request):
    book_list = BookInfo.objects.all()
    #hero_list = HeroInfo.objects.get(hbook=bid)
    return render(request,'booktest/show_book.html',{"book":book_list})

def detail(request,bid):
    book = BookInfo.objects.get(id=bid)
    hero_list = book.heroinfo_set.all()
    return render(request,'booktest/detail.html',{"hero":hero_list,"book":book})


# Create your views here.

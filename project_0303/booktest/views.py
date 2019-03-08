from django.shortcuts import render,redirect
from booktest.models import BookInfo,PicTest,AreaInfo
from project_0303 import settings
from django.http import HttpResponse

#装饰器：用户未登录，有些页面是不能访问的
def forbidGet(func):
    def set(request,*args,**kwargs):
        if request.session.has_key('islogin'):
            return func(request,*args,**kwargs)
        else:
            return redirect('/login')
    return set


# Create your views here.
def myfilter(request):
    context={'list':BookInfo.objects.all()}
    return render(request,'booktest/myfilter.html',context)


def block(request):
    return render(request,'booktest/child.html')


def login(request):
    '''login - page'''
    #判断用户是否已经成功登录过
    if request.session.has_key('islogin'):
        return render(request,'booktest/change_pwd.html')
    #服务器判断cookies中是否有记录的用户名
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
    else:
        username = ''
    return render(request,'booktest/login.html',{"username":username})


def logincheck(request):
    '''login check - page'''
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    if (username=="admin" and password=="123"):
        response = render(request,'booktest/change_pwd.html')
        #如果用户正确登录，告知浏览器设置cookies记录用户的登录名
        if remember == 'on':
            response.set_cookie('username',username)
        #使用session记录用户的登录状态，如果成功登录，短时间内登录不需要再次重新登录
        request.session['islogin'] = True
        #使用session记录用户的用户名
        request.session['username'] = username
        return response
    else:
        return redirect('/login')


@forbidGet
def changepwd(request):
    return render(request,'booktest/change_pwd.html')


@forbidGet
def changeover(request):
    #获取修改的密码
    password = request.POST.get('password')
    #获取session记录用户的名字
    username = request.session.get('username')
    return render(request,'booktest/changeover.html',{"pwd":password,"user":username})


def upload(request):
    return render(request,'booktest/upload_pic.html')


def upload_handle(request):
    pic = request.FILES['pic']
    save_path = '%s/booktest/%s'%(settings.MEDIA_ROOT,pic.name)
    with open(save_path,'wb') as f:
        for content in pic.chunks():
            f.write(content)
    PicTest.objects.create(goods_pic='booktest/%s'%pic.name)
    return HttpResponse('ok')

from django.core.paginator import Paginator
def show_area(request,page_num):
    area = AreaInfo.objects.filter(aParent__isnull=True)
    pp = Paginator(area,10)
    
    #nums = pp.num_pages
    rang = pp.page_range

    if page_num=='':
        index = 1
    else:
        index = int(page_num)
    content = pp.page(index)

    return render(request,'booktest/show_area.html',{"area":content,"range":rang})
    




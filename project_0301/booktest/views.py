from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse


# Create your views here.
def login(request):
    '''login - page'''
    return render(request,'booktest/login.html')


def logincheck(request):
    '''login check - page'''
    username = request.POST.get('username')
    password = request.POST.get('password')
    if (username=="admin" and password=="123"):
        return redirect('/login')
    else:
        return redirect('/login')


def ajax_test(request):
    return render(request,'booktest/ajax_test.html')


def ajax_handel(request):
    data = {"res":'cmm'}
    return JsonResponse(data)


def ajax_login(request):
    #判断用户是否成功登录过，如果成功登陆过，直接进入首页
    if request.session.has_key('islogin'):
        return HttpResponse('ok')
    else:
        #判断cookie中是否有需要的数据
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
        else:
            username = ''
        return render(request,'booktest/ajax_login.html',{'username':username})


def ajax_login_check(request):
    name = request.POST.get('username')
    pwd = request.POST.get('password')
    member = request.POST.get('member')
    if name == 'admin' and pwd == '123':
        #用户名和密码正确
        reponse = JsonResponse({'res':1})
        #设置session,记录用户成功登录
        request.session['islogin'] = True
        #设置cookie
        if member == 'on':
            reponse.set_cookie('username',name,max_age=3600)
        return reponse
    else:
        return JsonResponse({'res':0})
    

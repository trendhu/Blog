from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import json

# Create your views here.

def indexPage(request):
    return HttpResponseRedirect('/home/') 
#首页
def homePage(request):
    return render(request, "home.html")

#登录页面
def loginPage(request):
    return render(request, "login.html")

#about页面
def aboutPage(request):
    return render(request, "about.html")

#base页面
def blogPage(request):
    return render(request, "blog.html")

#contact页面
def contactPage(request):
    return render(request, "contact.html")

#portfolio页面
def portfolioPage(request):
    return render(request, "portfolio.html")


#文本比较工具页面
def textCompare(request):
    return render(request, "textCompare.html")



def loginApi(request):
    loginName = request.POST["username"]
    loginPassword = request.POST["password"]
    if (loginName == "hadoop" and loginPassword == "0"):
        return HttpResponse(json.dumps({'status':'ok'}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'status':'false'}), content_type="application/json")




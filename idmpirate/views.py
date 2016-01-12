from django.shortcuts import render
from django.http import HttpResponse
from models import BlogArticle
# Create your views here.
from django.contrib.auth import authenticate, login
def index(request):
    blogs = BlogArticle.objects.all()
    return render(request, "main.html", {'testvar':"Test String 2!",'blogs':blogs, 'user':None})

class Sign_in(object):
    '''This class is responsible for Login and Logout functionalities of users in controller'''
    def __init__(self):
        self.blogs=BlogArticle.objects.all()
    def sign_in(self,request):
        if request.method == 'POST':
            usname = request.POST['username']
            pwd = request.POST['password']
            user = authenticate(username=usname, password=pwd)
            if user is not None:
                login(request, user)
                return render(request, "main.html", {'testvar':"Test String 2!",'blogs':self.blogs, 'user':user} )
            else:
                #todo implement some register user dialog, modal, or forget password
                pass
        else:
            #todo use some cookies and browser data to auto sign in
            pass

class Blog(object):
    
    '''This class is responsible for controller functions i.e CRUD and  for Blog'''
    def createBlog(self,request):
        newBlog = BlogArticle()
        newBlog.title = request.POST['title']
        newBlog.author = request.user
        newBlog.blog_content = request.POST['blog_content']
        newBlog.save()
        blogs = BlogArticle.objects.all()
        return render(request, "main.html", {'testvar':"Test String 2!",'blogs':blogs, 'user':request.user} )
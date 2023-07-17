from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from .forms import *




# Create your views here.
def index(request):
    return render(request,"index.html")


def usersignup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        password = request.POST.get('password')
        # checking whether the username exists
        if User.objects.filter(
                username=username).first():  # the filter method is used to filter your search and allows you to return
            # only the rows that matches the search term
            # it will get first object from filter query.
            messages.success(request, 'username already taken')
            # message.success:is a framework that allows you to store messages in one request and retrive them in the request page
            return redirect(usersignup)
        if User.objects.filter(email=email).first():
            messages.success(request, 'email already exists')
            return redirect(usersignup)
        user_obj = User(username=username, email=email, first_name=firstname, last_name=lastname)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request, 'successfully registered')
    return render(request,"usersignup.html")


def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        request.session['username']=username
        user_obj=User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request,"user not found")
            return redirect(userlogin)
        user=authenticate(username=username,password=password)
        if user is None:
            messages.success(request,'wrong password or username')
            return redirect(userlogin)
        request.session['id'] = user_obj.id
        return redirect(home)
    return render(request,"userlogin.html")

# def musicupload(request):
#     if request.method == 'POST':
#         a = songuploadform(request.POST, request.FILES)
#         if a.is_valid():
#             fn=a.cleaned_data["filmname"]
#             mn=a.cleaned_data["musicname"]
#             im=a.cleaned_data["image"]
#             si=a.cleaned_data["singers"]
#             ln = a.cleaned_data["language"]
#             au = a.cleaned_data["audio"]
#             b=songupload(filmname=fn,musicname=mn,image=im,singers=si,language=ln,audio=au)
#             b.save()
#             request.session['id']=id
#             return HttpResponse("song upload successfully.....")
#         else:
#             return HttpResponse("song upload failed.....")
#     return render(request,"musicupload.html")


def home(request):
    a=songupload.objects.all().order_by('id')
    paginator = Paginator(a,8)
    page_number = request.GET.get('page')
    a = paginator.get_page(page_number)
    username = request.session['username']
    filmname=[]
    musicname=[]
    image=[]
    singers=[]
    language=[]
    audio=[]
    mid=[]
    for i in a:
        id = i.id
        mid.append(id)
        fn = i.filmname
        filmname.append(fn)
        mn = i.musicname
        musicname.append(mn)
        sg = i.singers
        singers.append(sg)
        ln= i.language
        language.append(ln)
        ai=i.audio
        audio.append(str(ai).split('/')[-1])
        im = i.image
        image.append(str(im).split('/')[-1])
    mylist=zip(filmname,musicname,image,singers,language,audio,mid)
    return render(request,"home.html",{'mylist':mylist,'a':a,'username':username})


def musicdisplay(request,id):
    a=songupload.objects.get(id=id)
    im = str(a.image).split('/')[-1]
    au = str(a.audio).split('/')[-1]
    return render(request,"musicdisplay.html",{'a':a,'im':im,'au':au,'id':id})


def likes(request,id):
    c = request.session['id']
    a = songupload.objects.get(id=id)
    if like.objects.filter(userid=c, musicname=a.musicname):
        messages.success(request,"already liked")
        return redirect(home)
    b = like(userid=c, filmname=a.filmname,musicname=a.musicname,singers=a.singers,image=a.image,audio=a.audio)
    b.save()
    messages.success(request, "liked")
    return redirect(home)

# def Likeview(request,pk):
#     post=get_object_or_404(songupload,id=request.POST.get('post_id'))
#     post.likes.add(request.user)
#     return HttpResponseRedirect(reverse('homes',args=[str(id)]))

def likedisplay(request):
    usid = request.session['id']
    username=request.session['username']
    a=like.objects.all()
    musicname=[]
    image=[]
    audio=[]
    mid=[]
    userid=[]
    for i in a:
        id = i.id
        mid.append(id)
        mn = i.musicname
        musicname.append(mn)
        ai=i.audio
        audio.append(str(ai).split('/')[-1])
        im = i.image
        image.append(str(im).split('/')[-1])
        usd=i.userid
        userid.append(usd)
    mylist=zip(musicname,image,audio,mid,userid)
    return render(request, "liked.html",{'mylist':mylist,'username':username,'usid':usid})

def liked(request,id):
    a=like.objects.get(id=id)
    im = str(a.image).split('/')[-1]
    au = str(a.audio).split('/')[-1]
    return render(request,"like.html",{'a':a,'im':im,'au':au,'id':id})

def likedelete(request,id):
    a=like.objects.get(id=id)
    a.delete()
    return redirect(likedisplay)

def user_logout(request):
    logout(request)
    return render(request,"index.html")



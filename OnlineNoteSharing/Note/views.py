from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout,login
from django.contrib.auth.models import User 
from .models import Signup, Notes
from datetime import date

# Create your views here.
def index(request):
    return render(request , 'index.html')

def about(request):
    return render(request , 'about.html')

def contact(request):
    return render(request , 'contact.html')

def login1(request):
    error=""
    if request.method=='POST':
        username=request.POST['email']
        password=request.POST['password']
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            error='no'
        else:
            error='yes'
    context={'error':error}
    return render(request , 'UserLogin.html', context)

def usercreation(request):
    error=''
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        contact = request.POST['contact']
        email = request.POST['email']
        password = request.POST['password']
        branch = request.POST['branch']
        role = request.POST['role']
        try:
            user = User.objects.create_user(username=email, password=password , first_name=fname, last_name= lname)
            Signup.objects.create(user=user ,contact=contact, branch=branch, role=role)
            error='no'
        except:
            error='yes'
    context ={
        "error":error
    }
    return render(request , 'usercreation.html',context)

def adminlogin(request):
    error=""
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['password']
        user= authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            error='no'
        else:
            error='yes'
    context={'error':error}
    return render(request , 'adminlogin.html',context)

def adminHome(request):
    if not request.user.is_staff:
        return redirect('adminlogin')
    else:
        accepted = Notes.objects.filter(status='Accepted').count()
        rejected = Notes.objects.filter(status='Rejected').count()
        panding = Notes.objects.filter(status='Panding').count()
        all = Notes.objects.all().count()
    context = {
        'accepted':accepted,'rejected':rejected, 'panding':panding,'all':all
    }
    return render(request , 'adminHome.html' , context)


def logout1(request):
        logout(request)
        return redirect("home")

def profile(request):
    if  not request.user.is_authenticated:
        return redirect('userlogin')
    else:
        user= User.objects.get(id=request.user.id)
        data= Signup.objects.get(user=user)
    context = {
        'user':user , 'data':data
    }
    return render(request , 'profile.html',context )
  
def changepassword(request):
    error=""
    if not request.user.is_authenticated:
        return redirect('userlogin')
    elif request.method == "POST":
        old = request.POST['oldp']
        new = request.POST['newp']
        con = request.POST['conp']
        if con==new:
            u=User.objects.get(username__exact =request.user.username)
            u.set_password(new)
            u.save()
            error="no"
        else:
            error="yes"
    context = {'error':error}
    return render(request , 'changepassword.html',context)

def editprofile(request):
    error =""
    if  not request.user.is_authenticated:
        return redirect('userlogin')
    user= User.objects.get(id=request.user.id)
    data= Signup.objects.get(user=user)
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        contact = request.POST['contact']
        branch = request.POST['branch']
        role = request.POST['role']
        try:
            user.first_name=fname
            user.last_name=lname
            data.contact=contact
            data.branch=branch
            data.role=role
            user.save()
            data.save()
            error="no"
        except:
            error ="yes"


    context = {
        'user':user , 'data':data,'error':error
    }
    return render(request , 'editprofile.html',context)
  
def uploadnotes(request):
    error =""
    if  not request.user.is_authenticated:
        return redirect('userlogin')
    if request.method == "POST":
        branch = request.POST['branch']
        subject = request.POST['subject']
        notesfile = request.FILES['notesfile']
        filetype = request.POST['filetype']
        discription = request.POST['discription']
        user = User.objects.filter(username=request.user.username).first()
        try:
            Notes.objects.create(user=user, uploadingdate=date.today() , branch=branch, subject= subject,
            notesfile=notesfile, filetype=filetype,discription= discription , status ='Panding')
           
            error='no'
        except:
            error='yes'
    context ={
        "error":error
    }
    return render(request , 'uploadnotes.html',context)

def mynotes(request):
    if  not request.user.is_authenticated:
        return redirect('userlogin')
    else:
        user= User.objects.get(id=request.user.id)
        notes= Notes.objects.filter(user=user)
    context = {
         'notes':notes
    }
    return render(request , 'mynotes.html',context )
  
def deletenote(request , id):
    if  not request.user.is_authenticated:
        return redirect('userlogin')
    else:
        notes= Notes.objects.filter(id=id)
        notes.delete()
        return redirect('mynotes')

def admindeletenote(request , id):
    if  not request.user.is_staff:
        return redirect('adminlogin')
    else:
        notes= Notes.objects.filter(id=id)
        notes.delete()
        return redirect('adminallnotes')
 
def userdelete(request , id):
    if  not request.user.is_staff:
        return redirect('adminlogin')
    else:
        user= Signup.objects.filter(id=id)
        user.delete()
        return redirect('alluser')
 

def allnotes(request):
    if  not request.user.is_authenticated:
        return redirect('userlogin')
    else:
        notes= Notes.objects.all()
    context = {
         'notes':notes
    }
    return render(request , 'allnotes.html',context )

def adminallnotes(request):
    if  not request.user.is_staff:
        return redirect('adminlogin')
    else:
        notes= Notes.objects.all()
    context = {
         'notes':notes
    }
    return render(request , 'adminallnotes.html',context )

def alluser(request):
    if  not request.user.is_staff:
        return redirect('adminlogin')
    else:
        user= Signup.objects.all()
    context = {
        'user':user
    }
    return render(request , 'alluser.html',context )

def pandingnotes(request):
    if  not request.user.is_staff:
        return redirect('adminlogin')
    else:
        notes= Notes.objects.filter(status='Panding')
    context = {
         'notes':notes ,'type':'View Panding Notes'
    }
    return render(request , 'notes.html',context )

def acceptednotes(request):
    if  not request.user.is_staff:
        return redirect('adminlogin')
    else:
        notes= Notes.objects.filter(status='Accepted')
    context = {
         'notes':notes,'type':'View Accepted Notes'
    }
    return render(request , 'notes.html',context )


def rejectednotes(request):
    if  not request.user.is_staff:
        return redirect('adminlogin')
    else:
        notes= Notes.objects.filter(status='Rejected')
    context = {
         'notes':notes,'type':'View Rejected Notes'
    }
    return render(request , 'notes.html',context )


def updatenotes(request,id):
    error =""
    if  not request.user.is_staff:
        return redirect('adminlogin')
    notes= Notes.objects.get(id=id)
    if request.method == "POST":
        branch = request.POST['branch']
        subject = request.POST['subject']
        filetype = request.POST['filetype']
        status = request.POST['status']
       
        try:
            notes.branch=branch
            notes.subject=subject
            notes.filetype=filetype
            notes.status=status
            notes.save()
            error="no"
        except:
            error ="yes"


    context = {
        'notes':notes,'error':error
    }
    return render(request , 'updatenotes.html',context)
  
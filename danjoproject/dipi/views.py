from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    data=User.objects.all()
    context={"data":data}
    return render(request,"index.html",context)


def insertData(request):
    
    if request.method=="POST":
        name= request.POST.get('name')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(name,lname,email,password)
        query= User(name=name,lname=lname,email=email,password=password)
        query.save()
        messages.warning(request,"Data Inserted Successfully ")
        return redirect("/")
    return render(request,"index.html")

def updateData(request,id):

    if request.method=="POST":
        name= request.POST['name']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        edit=User.objects.get(id=id)
        edit.name=name
        edit.lname=lname
        edit.email=email
        edit.password=password
        edit.save()
        messages.warning(request,"Data Updated Successfully")
        return redirect("/")

    d=User.objects.get(id=id)
    context={"d":d}
    return render(request,"edit.html",context)

def deleteData(request,id):
    d=User.objects.get(id=id)
    d.delete()
    messages.error(request,"Data deleted Successfully")
    return redirect("/")




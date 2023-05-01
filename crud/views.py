from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import StudentRegistration
from . models import User
# Create your views here.

# Add and show data
def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        # First way to save data in database.
        # if fm.is_valid():
        #     fm.save()

        # second way to save data in database.
        msg='Data Inserted successfully'
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)
            reg.save()
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()
    stu = User.objects.all()
    msg="Record Inserted Successfully..."
    return render(request,'enroll/addORshow.html',{'form':fm,'stu':stu,'msg':msg})

# delete data from database.

def del_data(request,id):
    if request.method =="POST":
        d = User.objects.get(pk=id)
        d.delete()
    return redirect('/')


# update data.

def update_data(request,id):
    return render(request,'enroll/update.html', {'id':id})

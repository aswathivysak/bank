from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import District,Branches,Country,City,Account_type,Materials,Gender,Form_data
import json
from django.http import JsonResponse
import datetime
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print('success')
            return redirect('formPage')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Wrong password')
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def formPage(request):
    districts = District.objects.all()
    accounts=Account_type.objects.all()
    materials=Materials.objects.all()
    gender=Gender.objects.all()
    context = {
        'districts': districts,
        'accounts' :accounts,
        'materials' : materials,
        'gender': gender,
    }
    if request.method == 'POST':
        list = []
        delimiter = ', '
        firstname = request.POST.get('first_name')

        lastname = request.POST.get('last_name')

        birthday = request.POST.get('dob','')

        display_format = '%m/%d/%Y'
        db_format = '%Y-%m-%d'
        db_date = datetime.datetime.strptime(birthday, display_format).strftime(db_format)

        age = request.POST.get('age')

        phone = request.POST.get('phone')

        account = request.POST.get('account')

        distri = request.POST.get('country')
        district=District.objects.get(id=distri)

        bran = request.POST.get('city')
        branch = Branches.objects.get(id=bran)

        gender = request.POST.get('gender')

        email = request.POST.get('email')

        address = request.POST.get('address')


        checked = request.POST.getlist('check[]')
        for i in checked:
            material = Materials.objects.get(id=i)
            list.append(str(material))
        materials = delimiter.join(list)

        form=Form_data(firstname=firstname,lastname=lastname,birthday= db_date,age=age,phone_num=phone,account_type=account,district=district,branch=branch,gender=gender,email=email,address=address,materials=materials)
        form.save()
        print("you are saved")
        messages.info(request, 'Your application accepted...')
        return redirect('formPage')
    return render(request,'form2.html',context=context)

def ajax_handler(request,id):
    branches = Branches.objects.filter(dist__id=id).values_list('id','branch')
    print(branches)
    branches = dict(branches)
    return JsonResponse({
        'branches' : branches,
    })
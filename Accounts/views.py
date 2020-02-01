from django.shortcuts import render,redirect
from .form import GirisForm,Qeydiyyat
from django.contrib.auth import authenticate,login

# Create your views here.
def Giris(requset):
    girisform=GirisForm(requset.POST or None)
    if girisform.is_valid():
        username=girisform.cleaned_data.get('username')
        password=girisform.cleaned_data.get('password')
        user=authenticate(username=username,password=password)
        login(requset,user)
        return redirect('index')

    content ={
        'giris':girisform
    }

    return render(requset,'giris.html',content)

def QeydiyyatView(request):
    form=Qeydiyyat(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        password=form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        return redirect('home')
    content={
        'qeydiyyat':form
    }
    return render(request,'uzv_ol.html',content)


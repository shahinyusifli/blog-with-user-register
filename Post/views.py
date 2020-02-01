from django.shortcuts import render,redirect,get_object_or_404,Http404
from .models import Postlar
from .form import YaratForm

# Create your views here.
# Ev is 'home ' in my language
def Ev(request):
    return render(request,'ev.html')

def Index(request):
    postlar=Postlar.objects.all()
    content={
        'postlar':postlar
    }
    return render(request,'index.html',content)

def Detay(request,id):
    post=get_object_or_404(Postlar,id=id)
    content={
        'post':post
    }
    return render(request,'detay.html',content)

def Yarat(request):
    if not request.user.is_authenticated():
        return Http404()

    form=YaratForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    content={
        'form':form,

    }
    return render(request,'yarat.html',content)

def Update(request,id):
    if not request.user.is_authenticated():
        return Http404()

    post=get_object_or_404(Postlar,id=id)
    form=YaratForm(request.POST or None,instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    content={
        'form':form
    }
    return render(request,'yarat.html',content)


from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def dehatimotor(request):
    return render(request,'dehatimotor.html')

def motor(request):
    return render(request,'motor.html')

def sheetbody(request):
    return render(request,'sheetbody.html')

def indiamark(request):
    return render(request,'indiamark.html')

def rollpipe(request):
    return render(request,'rollpipe.html')

def submersible(request):
    return render(request,'submersible.html')

def pump(request):
    return render(request,'pump.html')

def cowmat(request):
    return render(request,'cowmat.html')

def blog(request):
    return render(request,'blog.html')


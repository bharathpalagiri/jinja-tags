from django.shortcuts import render

# Create your views here.
def reddy(request):
    d={'name':'bharath','age':22}
    return render(request,'bharath.html',context=d)
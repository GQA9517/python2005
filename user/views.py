from django.shortcuts import render,HttpResponse
# Create your views here.



def test():
    print(111)
    print(222)
    print(999)
    return HttpResponse('测试')


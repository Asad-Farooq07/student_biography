from django.shortcuts import render

# Create your views here.
def add_show(request):
    return render(request,'enroll/addandshow.html')

def show_base(request):
    return render(request,'enroll/base.html')

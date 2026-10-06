from django.shortcuts import render

# App2 views here.
def base(request):
    return render(request,'base.html')


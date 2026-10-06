from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

# App2  views here.

@login_required
def gotoEmpDashboard(request):
    return render(request, 'empdash.html')


def signup(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check Password
        if password != confirm_password:
            messages.error(request, "Please enter similar passwords")
            return redirect("signup")

        # Check Username
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")

        # Check Email
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("signup")

        # Create User
        u = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        print(u)
        login(request,u)

        u.set_password(password)
        u.save()

        messages.success(request, "Username registered successfully")
        return redirect("index")

    return render(request, 'signup.html')
def emplogin(request):
    if request.method == 'POST':
        u=request.POST.get('uname')
        p=request.POST.get('password')

        #username and password authentication
        x=authenticate(username=u,password=p)
    
        
        if x is not None:

            login(request,x)
            #create session id
            request.session['username']=u
            print('session id -->',u)
            request.session.set_expiry(30)
            return redirect("gotoEmpdashboard")
    
        messages.error(request,"please enter correct username or password")
        return redirect("login")

    return render(request,'login.html')
@login_required
def llogout(request):
    logout(request)

    request.session.flush()
    return redirect('base')


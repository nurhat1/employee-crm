from django.shortcuts import render, redirect

#django login and register
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#my imports: decorators, forms
from .forms import CreateUserForm
from .decorators import unauthenticated_user

#messages
from django.contrib import messages

# Create your views here.


#-----------------------Register------------------------
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            #Send message about success registration
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')


    context = {'form': form}
    return render(request, 'accounts/register.html',  context)




#--------------Login--------------------
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'accounts/login.html')




#-----------LOGOUT--------------------
def logoutUser(request):
    logout(request)
    return redirect('login')




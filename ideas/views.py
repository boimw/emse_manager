from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Idea, User, Rating
# Create your views here.

def index(request):
	return render(request, 'ideas/home.html')

def login(request):
	if request.method == 'POST':

	#collecting form data
		username = request.POST.get('username')
		password = request.POST.get('password')
		# checking for user first
		user = authenticate(username=username, password=password)
		print (user)
		if user is not None:
			if user.is_active:
				user = User.objects.get(username=username)
				auth_login(request, user)
				return HttpResponseRedirect(reverse('home'))
			else:
				return render(request, 'ideas/login.html', {'error_message': "Account is not activated!"})
		else:
			return render(request, 'ideas/login.html', {'error_message': "Wrong Email address or Password!"})
	else:
		return render(request, 'ideas/login.html')

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))

def register(request):
    return render(request, 'ideas/register.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('cpassword')
        if password == password_confirm:
            users = User.objects.all()
            for u in users:
                if u.username == username:
                    return render(request, 'ideas/register.html', context={
                        'error_message':"User already exists!"
                    })
            new_user = User.objects.create_user(username, username, password)
            new_user.is_staff = False
            new_user.is_active = True
            new_user.is_superuser = False
            new_user.save()
            return render(request, 'ideas/register.html', context={
                'info_message': "Account created successfully. Now you can login with you account!"
            })
        else:
            return render(request, 'ideas/register.html', context={
                'error_message': "Password does not match the confirm password."
                })

@login_required(login_url='/')
def profile(request, user_id):
    this_user = get_object_or_404(User, pk=user_id)
    right_now = timezone.now()
    return render(request, 'ideas/profile.html', context={
        'user': this_user,
        'time': right_now
        })

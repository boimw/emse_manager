from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from profiles.models import profile

# Create your views here.
def home(request):
	context = {}
	template = 'home.html'
	return render(request,template,context)
def about(request):
	context = {}
	template = 'about.html'
	return render(request,template,context)

@login_required(login_url='/accounts/login/')
def userProfile(request):
	user = request.user
	context = {'user': user}
	template = 'profile.html'
	return render(request,template,context)

@login_required(login_url='/accounts/login/')
def edit(request, user_id):
	user = request.user
	first_name = request.POST.get('first_name')
	last_name = request.POST.get('last_name')
	address = request.POST.get('address')
	email = request.POST.get('email')
	user.first_name = first_name
	user.last_name = last_name
	user.email = email
	user.save()
	return render(request, 'profile.html', context={
                'info_message': "Successfully!"
                })

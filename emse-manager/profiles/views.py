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
	user_profile = profile.objects.get(user=user)
	context = {'user': user, 'user_profile': user_profile}
	template = 'profile.html'
	return render(request,template,context)

@login_required(login_url='/accounts/login/')
def edit(request, user_id):
	user = request.user
	user_profile = profile.objects.get(user=user)
	first_name = request.POST.get('first_name')
	last_name = request.POST.get('last_name')
	address = request.POST.get('address')
	user.first_name = first_name
	user.last_name = last_name
	user_profile.address = address
	user.save()
	user_profile.save()
	return render(request, 'profile.html', context={
                'info_message': "Successfully!", 'user_profile': user_profile
                })

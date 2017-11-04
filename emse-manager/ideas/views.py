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

def ideas(request):
	ideas = Idea.objects.all
	context = {'ideas': ideas}
	template = 'ideas.html'
	return render(request, template, context)
	
def idea(request, idea_id):
    idea = Idea.objects.get(id=idea_id)
    context = {'idea': idea}
    template = 'idea.html'
    return render(request,template,context)
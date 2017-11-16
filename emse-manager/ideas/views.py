from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Idea, User, Rating, Category
from carts.cart import Cart 
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

def categories(request):
	categories = Category.objects.all
	context = {'categories': categories}
	template = 'categories.html'
	return render(request, template, context)

def category(request, category_id):
	category = Category.objects.get(id=category_id)
	context = {'category': category}
	template = 'categories.html'
	return render(request, template, context)

def create_category_view(request):
	template = 'createCategory.html'
	return render(request, template)

def create_category(request):
	category_name = request.POST.get('category_name')
	category_description = request.POST.get('category_description')
	if(category_name  and category_description):
		category = Category.objects.create(name = category_name, description = category_description)
		category.save()

	categories = Category.objects.all
	return render(request, 'categories.html', context={
                'info_message': "Successfully!", 'categories': categories
                })

@login_required(login_url='/accounts/login/')
def create(request):
	categories = Category.objects.all
	context = { 'categories': categories }
	template = 'create.html'
	return render(request, template, context)

@login_required(login_url='/accounts/login/')
def create_idea(request):
	user = request.user
	idea_name = request.POST.get('idea_name')
	idea_description = request.POST.get('idea_description')
	idea = Idea.objects.create(name = idea_name, description = idea_description, owner = user, catId = Category.objects.latest('id'))
	idea.save()
	ideas = Idea.objects.all
	return render(request, 'ideas.html', context={
                'info_message': "Successfully!", 'user': user, 'ideas': ideas
                })

	return render(request)

@login_required(login_url='/accounts/login/')
def edit(request,idea_id):
	idea=Idea.objects.get(id=idea_id)
	context = {'idea': idea}
	template = 'edit.html'
	return render(request, template, context)

@login_required(login_url='/accounts/login/')
def update(request,idea_id):
	idea=Idea.objects.get(id=idea_id)
	idea_name = request.POST.get('idea_name')
	idea_description = request.POST.get('idea_description')
	idea.name = idea_name
	idea.description = idea_description
	idea.save()
	return render(request, 'idea.html', context={
                'info_message': "Successfully!", 'idea': idea
                })



@login_required(login_url='/accounts/login/')
def add_to_cart(request, idea_id):
	idea = Idea.objects.get(id=idea_id)
	quantity = request.POST.get('quantity')
	cart = Cart(request)
	cart.add(idea, idea.price, quantity)
	return render(request, 'cart.html', context={
                'info_message': "Successfully!", 'cart': cart
})

@login_required(login_url='/accounts/login/')
def remove_from_cart(request, idea_id):
    idea = Idea.objects.get(id=idea_id)
    cart = Cart(request)
    cart.remove(idea)
    return render(request, 'cart.html', context={
                'info_message': "Successfully!", 'cart': cart
})

@login_required(login_url='/accounts/login/')
def cart(request):
	cart = Cart(request)
	context = {'cart':cart}
	template = 'cart.html'
	return render(request,template,context)
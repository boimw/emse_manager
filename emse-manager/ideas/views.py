from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate
from django.db.models import Q
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Idea, User, Rating, Category, Comment
from carts.cart import Cart 
# Create your views here.

def ideas(request):
	ideas_list = Idea.objects.all()
	paginator = Paginator(ideas_list, 5) # Show 10 ideas per page

	page = request.GET.get('page')
	try:
		ideas = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		ideas = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		ideas = paginator.page(paginator.num_pages)

	context = {'ideas': ideas}
	template = 'ideas.html'
	return render(request, template, context)
	
def idea(request, idea_id):
	idea = Idea.objects.get(id=idea_id)
	try:
		comments = Comment.objects.filter(idea=idea)
	except Comment.DoesNotExist:
		comments = None
	
	context = {'idea': idea, 'comments': comments }
	template = 'idea.html'
	return render(request,template,context)

def vote_up(request, idea_id):
	user = request.user
	idea = Idea.objects.get(id=idea_id)
	idea.votes.up(user.id)
	return HttpResponseRedirect(reverse('idea', kwargs={'idea_id':idea.id}))

def vote_down(request, idea_id):
	user = request.user
	idea = Idea.objects.get(id=idea_id)
	idea.votes.down(user.id)
	return HttpResponseRedirect(reverse('idea', kwargs={'idea_id':idea.id}))

def categories(request):
	categories = Category.objects.all
	context = {'categories': categories}
	template = 'categories.html'
	return render(request, template, context)

def category(request, category_id):
	category = Category.objects.get(id=category_id)
	ideas = Idea.objects.all
	context = {'category': category, 'ideas': ideas}
	template = 'category.html'
	return render(request, template, context=context)

@login_required(login_url='/accounts/login/')
def delete_category(request, category_id):
	category = Category.objects.get(id=category_id)
	category.delete()
	categories = Category.objects.all
	context = {'categories': categories}
	template = 'categories.html'
	return render(request, 'categories.html', context={
                'info_message': "Category deleted", 'categories': categories
                })

@login_required(login_url='/accounts/login/')
def add_comment(request, idea_id):
	user = request.user
	comment_idea=Idea.objects.get(id=idea_id)
	comment_text = request.POST.get('comment_text')
	
	if(comment_text):
		comment = Comment.objects.create(comment = comment_text,  owner = user, idea=comment_idea)
		comment.save()
	comments = Comment.objects.filter(idea=comment_idea)
	return render(request, 'idea.html', context={
                'info_message': "Successfully!", 'idea': comment_idea, 'comments': comments
                })

@login_required(login_url='/accounts/login/')
def edit_category(request, category_id):
	category=Category.objects.get(id=category_id)
	context = {'category': category}
	template = 'editCategory.html'
	return render(request, template, context)

@login_required(login_url='/accounts/login/')
def update_category(request, category_id):
	category=Category.objects.get(id=category_id)
	category_name = request.POST.get('category_name')
	category_description = request.POST.get('category_description')
	category.name = category_name
	category.description = category_description
	category.save()
	categories = Category.objects.all
	template = 'categories.html'
	return render(request, template, context={
                'info_message': "Category updated", 'categories': categories
                })

@login_required(login_url='/accounts/login/')
def create_category_view(request):
	template = 'createCategory.html'
	return render(request, template)

@login_required(login_url='/accounts/login/')
def create_category(request):
	category_name = request.POST.get('category_name')
	category_description = request.POST.get('category_description')
	if(category_name  and category_description):
		category = Category.objects.create(name = category_name, description = category_description)
		category.save()

	categories = Category.objects.all
	return render(request, 'categories.html', context={
                'info_message': "Category created", 'categories': categories
                })

def search(request):
	search = request.POST.get('searchbox')
	ideas_list = Idea.objects.filter(Q(name__contains=search) | Q(description__contains=search))
	
	paginator = Paginator(ideas_list, 5) # Show 10 ideas per page

	page = request.GET.get('page')
	try:
		ideas = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		ideas = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		ideas = paginator.page(paginator.num_pages)

	context = {'ideas': ideas}
	template = 'ideas.html'
	return render(request, template, context)

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
	idea_category = request.POST.get('category_select')
	idea_on_sale = request.POST.get('on_sale')
	idea_price = request.POST.get('price')
	idea = Idea.objects.create(name = idea_name, description = idea_description, owner = user, catId = Category.objects.get(id=idea_category), on_sale = idea_on_sale, price = idea_price)
	idea.save()
	ideas_list = Idea.objects.all()
	paginator = Paginator(ideas_list, 5) # Show 10 ideas per page

	page = request.GET.get('page')
	try:
		ideas = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		ideas = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		ideas = paginator.page(paginator.num_pages)

	context = {'info_message': "Idea successfully created", 'user': user, 'ideas': ideas}
	return render(request, 'ideas.html', context=context)


@login_required(login_url='/accounts/login/')
def edit(request,idea_id):
	idea=Idea.objects.get(id=idea_id)
	categories = Category.objects.all
	context = {'idea': idea, 'categories': categories }
	template = 'edit.html'
	return render(request, template, context)

@login_required(login_url='/accounts/login/')
def delete(request,idea_id):
	idea=Idea.objects.get(id=idea_id)
	idea.delete()
	ideas_list = Idea.objects.all()
	paginator = Paginator(ideas_list, 5) # Show 10 ideas per page
	page = request.GET.get('page')
	try:
		ideas = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		ideas = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		ideas = paginator.page(paginator.num_pages)

	user = request.user
	return render(request, 'ideas.html', context={
                'info_message': "Idea deleted", 'user': user, 'ideas': ideas
                })

@login_required(login_url='/accounts/login/')
def update(request,idea_id):
	idea=Idea.objects.get(id=idea_id)
	idea_name = request.POST.get('idea_name')
	idea_description = request.POST.get('idea_description')
	idea_category = request.POST.get('category_select')
	idea_on_sale = request.POST.get('on_sale')
	idea_price = request.POST.get('price')
	idea.name = idea_name
	idea.description = idea_description
	idea.catId = Category.objects.get(id=idea_category)
	idea.on_sale = idea_on_sale
	idea.price = idea_price
	idea.save()
	ideas_list = Idea.objects.all()

	paginator = Paginator(ideas_list, 5) # Show 10 ideas per page

	page = request.GET.get('page')
	try:
		ideas = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		ideas = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		ideas = paginator.page(paginator.num_pages)

	user = request.user
	return render(request, 'ideas.html', context={
                'info_message': "Idea successfully updated", 'user': user, 'ideas': ideas
                })



@login_required(login_url='/accounts/login/')
def add_to_cart(request, idea_id):
	idea = Idea.objects.get(id=idea_id)
	cart = Cart(request)
	cart.add(idea, idea.price)
	return render(request, 'cart.html', context={
                'info_message': "Idea added successfully!", 'cart': cart
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
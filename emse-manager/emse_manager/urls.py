"""emse_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

from ideas import views as ideas_views
from profiles import views as profiles_views
from checkout import views as checkout_views

urlpatterns = [
	url(r'^$', profiles_views.home, name='home'), 
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^about/$', profiles_views.about, name='about'),
    url(r'^profile/$', profiles_views.userProfile, name='profile'),
    url(r'^edit/(?P<user_id>[0-9]+)/$', profiles_views.edit, name='edit'),
    url(r'^checkout/$', checkout_views.checkout, name='checkout'), 
	url(r'^ideas/$', ideas_views.ideas, name='ideas'),
    url(r'^categories/$', ideas_views.categories, name='categories'),
    url(r'^ideas/search/$', ideas_views.search, name='idea_search'),
    url(r'^ideas/new/$', ideas_views.create, name='create'),
    url(r'^ideas/create_idea/$', ideas_views.create_idea, name='create_idea'),
    url(r'^edit_idea/(?P<idea_id>[0-9]+)/edit/$', ideas_views.edit, name='edit_idea'),
    url(r'^update_idea/(?P<idea_id>[0-9]+)/update/$', ideas_views.update, name='update_idea'),
    url(r'^ideas/(?P<idea_id>[0-9]+)/delete/$', ideas_views.delete, name='delete_idea'),
    url(r'^categories/new_category/$', ideas_views.create_category, name='new_category'),
    url(r'^ideas/new_category_view/$', ideas_views.create_category_view, name='create_category'),
    url(r'^cart/$', ideas_views.cart, name='cart'), 
    url(r'^idea/(?P<idea_id>[0-9]+)/$', ideas_views.idea, name='idea'),
    url(r'^idea/(?P<idea_id>[0-9]+)/vote_up/$', ideas_views.vote_up, name='idea_vote_up'),
    url(r'^idea/(?P<idea_id>[0-9]+)/vote_down/$', ideas_views.vote_down, name='idea_vote_down'),
    url(r'^idea/(?P<idea_id>[0-9]+)/comment/$', ideas_views.add_comment, name='add_comment'),
    url(r'^idea/(?P<idea_id>[0-9]+)/comment/edit/(?P<comment_id>[0-9]+)/$', ideas_views.edit_comment, name='edit_comment'),
    url(r'^idea/(?P<idea_id>[0-9]+)/comment/(?P<comment_id>[0-9]+)/$', ideas_views.comment_for_edit, name='comment_for_edit'),
    url(r'^idea/(?P<idea_id>[0-9]+)/comment/delete/(?P<comment_id>[0-9]+)/$', ideas_views.delete_comment, name='delete_comment'),
    url(r'^idea/(?P<idea_id>[0-9]+)/comment/like/(?P<comment_id>[0-9]+)/$', ideas_views.like_comment, name='like_comment'),
    url(r'^category/(?P<category_id>[0-9]+)/$', ideas_views.category, name='category'),
    url(r'^category/(?P<category_id>[0-9]+)/edit/$', ideas_views.edit_category, name='edit_category'),
    url(r'^category/(?P<category_id>[0-9]+)/update/$', ideas_views.update_category, name='update_category'),
    url(r'^category/(?P<category_id>[0-9]+)/delete/$', ideas_views.delete_category, name='delete_category'),
    url(r'^add_to_cart/(?P<idea_id>[0-9]+)/$', ideas_views.add_to_cart, name='add_to_cart'),
    url(r'^remove_from_cart/(?P<idea_id>[0-9]+)/$', ideas_views.remove_from_cart, name='remove_from_cart'),
    url(r'^accounts/', include('allauth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

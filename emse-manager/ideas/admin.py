from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Idea
class IdeaAdmin(admin.ModelAdmin):
	class Meta:
		model = Idea
		
admin.site.register(Idea,IdeaAdmin)

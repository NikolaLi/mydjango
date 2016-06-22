from django.contrib import admin

# Register your models here.
from .models import Choice,Question

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	# fields = ['pub_date','question_text']
	fieldsets = [
		(None, 				{'fields':['question_text']}),
		('Date information',{'fields':['pub_date'],'classes':['collapse']})
	]
	inlines = [ChoiceInline]
	#show field
	list_display = ('question_text','pub_date','was_published_recently')
	# filter
	list_filter = ['pub_date']
	#search 
	search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)
from django.contrib import admin

# Register your models here.

from .models import Choice,Question

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fileds = [
		(None,{'fileds':['question_text']}),
		('Date information',{'fields':['pubd_date'],'classes':['collapse']}),
	]
	inlines=[ChoiceInline]

admin.site.register(Question,QuestionAdmin)

admin.site.register(Choice)

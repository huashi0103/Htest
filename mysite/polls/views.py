from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.views import generic
from django.urls import reserse
# Create your views here.
from .models import Question

def IndeView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	
	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]
	# latest_question_list =Question.objects.order_by('-pub_date')[:5]
	# template=loader.get_template('polls/index.html')
	# context={'latest_question_list':latest_question_list}
	# print(context)
	# return render(request,'polls/index.html',context)

def DetailView(generic.DetailView):
	try:
		question=Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise http404("Question does not exist")
	#import django.shortcuts import get_object_or_404
	#question = get_object_or_404(Question,pk=question_id)
	return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
	question=get_object_or_404(Question,pk=question_id)
	return render(request,'pools/results.html',{'question':question})

def vote(request,question_id):
	quetion = get_object_or_404(Question,pk=question_id)
	try:
		selected_choice=question.choice_set.get(pk=request.POST['choice'])
	except(KeyError,Choice.DoesNotExist):
		return render(request,'pools.detail.html',{
			'question':question,
			'error_message':"You didn't select a choice.",
		})
	else:
		selected_choice.votes+=1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
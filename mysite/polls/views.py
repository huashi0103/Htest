from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.views import generic
from django.urls import reverse
from django.utils import timezone
# Create your views here.
from .models import Choice,Question

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	
	def get_queryset(self):
		'''return the last five published questions''' 
		return Question.objects.filter(
		pub_date__lte=timezone.now()
		).order_by('-pub_date')[:5]
	# latest_question_list =Question.objects.order_by('-pub_date')[:5]
	# template=loader.get_template('polls/index.html')
	# context={'latest_question_list':latest_question_list}
	# print(context)
	# return render(request,'polls/index.html',context)

class DetailView(generic.DetailView):
	model=Question
	template_name='polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name='polls/results.html'

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
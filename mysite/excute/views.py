from django.shortcuts import render
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from mysite import settings
import os

def index(request):
	batpath=settings.BAT_PATH
	bat_list=[]
	for file in os.listdir(batpath):
		if os.path.splitext(file)[1] == '.bat':
			bat_list.append(file)
	context={'bat_list':bat_list}
	print(os.path.abspath('.'))
	return render(request,'mysite/index.html',context)
	#return HttpResponse("You're looking at question %s." % bat_list)
	
def execute(bat):
	return HttpResponse("You're looking at question %s." % bat)
	

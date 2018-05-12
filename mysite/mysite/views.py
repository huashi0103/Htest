from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

from . import settings
import os

def index(request):
	return render(request,'mysite/index.html')
	#return HttpResponse("You're looking at question %s." % bat_list)


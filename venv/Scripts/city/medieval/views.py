from django.shortcuts import render
from .models import *
 
def index(request):
	statuss=status.objects.all()
	feodalss=feodals.objects.all()
	seniorss=seniors.objects.all()
	citizenss=citizens.objects.all()

	return render(request, 'medieval/index.html', locals())
 


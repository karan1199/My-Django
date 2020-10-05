from django.shortcuts import render,HttpResponse
from .models import Project
from django.contrib import messages


# Create your views here.
def index(request):

    return render(request,'index.html')
    
def about(request):
    return render(request,'about.html')

def skills(request):
    return render(request,'skills.html')

def projects(request):
	project=Project.objects.all()
	return render(request,'projects.html', {'projects':project})


def contact(request):
	if request.method =='POST':
		messages.success(request, 'Your response has been recorded. Thanks for your feedback.') 
	return render(request, 'contact.html')
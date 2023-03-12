from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request=request, template_name='anasite/index.html')

def about(request):
	return render(request=request, template_name='anasite/about.html')

def projects(request):
	return render(request=request, template_name='anasite/projects.html')

def resume(request):
	return render(request=request, template_name='anasite/resume.html')

def contact(request):
	return render(request=request, template_name='anasite/contact.html')
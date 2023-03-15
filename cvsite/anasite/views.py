from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request=request, template_name='anasite/home.html')

def about(request):
	return render(request=request, template_name='anasite/about.html')

def projects(request):
	return render(request=request, template_name='anasite/projects.html')

def resume(request):
	return render(request=request, template_name='anasite/resume.html')

def contact(request):
	return render(request=request, template_name='anasite/contact.html')

def homept(request):
	return render(request=request, template_name='anasite/homept.html')

def sobre(request):
	return render(request=request, template_name='anasite/sobre.html')
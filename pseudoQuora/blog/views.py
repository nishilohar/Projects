from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.core.mail import send_mail

from . import models
from . import forms

# Create your views here.

def home(request):
	results = models.QuestionAndAnswer.objects.filter().order_by('id')[::-1]
	print (results)
	paginator = Paginator(results,2)
	page = request.GET.get('page')
	try:
		p = paginator.page(page)
	except PageNotAnInteger:
		p = paginator.page(1)
	except EmptyPage:
		p = paginator.page(paginator.num_pages)
	# return HttpResponse("Welcome Home")
	return render(request, "home.html",{'blog_data':p})


def ask(request):
	title = "Ask Question"
	form = forms.QuestionForm(request.POST or None)
	confirmMessage = None
	if form.is_valid():
		formObj = models.QuestionAndAnswer.objects.create(
				question = form.cleaned_data['question'],
				askedBy = form.cleaned_data['name']
			)
		title = ""
		confirmMessage = "Thanks for asking question"
		formObj.save()
		form = None
	context = {
	'title': title,
	'form':form,
	'confirmMessage':confirmMessage,
	}
	return render(request, "ask.html",context)

def login(request):
	title = "Login"
	form = forms.LoginForm(request.POST or None)
	if form.is_valid():
		user_name = form.cleaned_data['username']
		password = form.cleaned_data['password']
		form = None
		title = None
	context = {
		'title': title,
		'form':form,
	}
	return render(request, "login.html",context)

def contact(request):
	# subject = "This is subject"
	# message = "this is sample message"
	# sender = 'nishilohar@gmail.com'
	# recipient = ['nishilohar@hotmail.com']
	# send_mail(subject, message, sender, recipient)
	# return HttpResponse("Email send successfully")

	title = "Contact"
	form = forms.ContactForm(request.POST or None)
	confirmMessage = None
	if form.is_valid():
		subject = "This is new subject"
		name = form.cleaned_data['name']
		email = form.cleaned_data['email']
		message = form.cleaned_data['message']
		recipient = ['nishilohar@gmail.com']
		send_mail(name, message, email, recipient)
		form = None
		title = None
		confirmMessage = "Thanks For Reaching Out"
	context = {
	'title': title,
	'form': form,
	'confirmMessage': confirmMessage
	}
	return render(request, "contact.html", context)
from django.shortcuts import render, HttpResponse, redirect
from models import *
import bcrypt
import re
from django.contrib import messages 
  # the index function is called when root is visited
def index(request):
    return render(request, 'nip/login.html')

def new_user(request):
	errors = User.objects.regis_basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	email = request.POST['email']
	image = request.POST['picture']
	password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
	User.objects.create(first_name=first_name, last_name=last_name, email=email, image=image,password=password)
	request.session['id'] = User.objects.get(email=email).id
	return redirect('/socials')

def login(request):
	errors = User.objects.log_basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')
	email = request.POST['email']
	request.session['id'] = User.objects.get(email=email).id
	context = {
		'picture': User.objects.get(id=request.session['id']).image,
		'name': User.objects.get(id=request.session['id']).first_name
	}
	return render(request,'nip/home.html',context)


def strength(request):
    context = {
        'stacks': Stack.objects.all()
    }
    return render(request, 'nip/strengths.html', context)

def socials(request):
	print request.session['id']
	return render(request, 'nip/registration.html')

def socials_process(request):
	errors = {}
	if len(request.POST['linkedin']) < 1:
		errors['linkedin'] = 'LinkedIn field is mandatory :)'
	# if len(request.POST['type']) < 1:
	# 	errors['post'] = 'Please answer if you are an instructor or student'
	if len(request.POST['github']) < 1:
		errors['github'] = 'GitHub field is mandatory :)'
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/socials')
	status = request.POST['type']
	linkedin = request.POST['linkedin']
	facebook = request.POST['facebook']
	github = request.POST['github']
	slack = request.POST['slack']
	instagram = request.POST['instagram']
	twitter = request.POST['twitter']
	user = User.objects.get(id=request.session['id'])
	user.status = status
	user.linkedin = linkedin
	user.facebook = facebook
	user.github = github
	user.slack = slack
	user.instagram = instagram
	user.twitter = twitter
	user.save()
 	return redirect('/strengths')

def home(request):
	return render(request,'nip/home.html')	 

def process(request):
	if request.method == "POST":
		user = User.objects.get(id=request.session["id"])
		for id in request.POST.getlist['sCheck']:
			user.strengths.add(id=id)	 
		return redirect('/home')







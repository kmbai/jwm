from django.shortcuts import render
from django.views.generic import ListView
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings


def home(request):
	return render(request,'jwm/home.html')

def contact(request):
	if request.method == 'POST':
		message = request.POST['message']
		email2 = 'enquiries@jwmandassociates.com'
		name = request.POST['name']
		subject = request.POST['subject']
		send_mail(name, message,'settings.EMAIL_HOST_USER',
			[email2],
			fail_silently=False)
	return render(request,'jwm/contact.html')

def gallery(request):
	return render(request,'jwm/gallery.html')

def services(request):
	return render(request,'jwm/services.html')

def financial(request):
	return render(request,'jwm/financial.html')

def taxation(request):
	return render(request,'jwm/taxation.html')

def companysecretary(request):
	return render(request,'jwm/companysecretary.html')

def audit(request):
	return render(request,'jwm/audit.html')

def administration(request):
	return render(request,'jwm/administration.html')

def hr(request):
	return render(request,'jwm/hr.html')


def aboutus(request):
	return render(request,'jwm/whatwedo.html')

def careers(request):
	return render(request,'jwm/careers.html')

def bookkeeping(request):
	return render(request,'jwm/bookkeeping.html')

def others(request):
	return render(request,'jwm/others.html')

def location(request):
	return render(request,'jwm/location.html')








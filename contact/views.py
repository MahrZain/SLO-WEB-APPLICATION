from django.shortcuts import render, redirect
from django.contrib import messages
import requests
import json
from .models import Contact, Usrinfo

def contact(request):
    info = Usrinfo.objects.all()
    print(info)
    data = {
        'info': info,
        'active_nav': 'contact'
    }
    return render(request, 'contactf.html',data)

def savecontact(request):
    # Check honeypot fields
    if request.POST.get('honeypot_name') or request.POST.get('honeypot_email'):
        return render(request, 'contactf.html', {'error': 'Bot detected'})

    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    
    # Check if required fields are filled
    if not name or not email or not message:
        messages.error(request, 'Please Fill All The Fields!')
        return render(request, 'contactf.html')
    else:
        contact = Contact(name=name, email=email,message=message)
        contact.save()
        messages.success(request, 'Sent Successfully!')
        return redirect('contact')  # Redirect to the contact page or another page of your choice
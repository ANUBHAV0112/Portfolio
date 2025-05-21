from django.shortcuts import render, redirect
from .models import Project, Contact
from .forms import ContactForm
import os

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                contact = form.save()
                print("Contact saved:", contact)
                return redirect('contact_success')
            except Exception as e:
                print("🔥 Error saving contact:", e)
        else:
            print("Form Errors:", form.errors)
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')

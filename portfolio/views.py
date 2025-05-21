from django.shortcuts import render, redirect
from .models import Project, Contact
from .forms import ContactForm
import os
import logging

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})


logger = logging.getLogger(__name__)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                contact = form.save()
                logger.info("Contact saved: %s", contact)
                return redirect('contact_success')
            except Exception as e:
                logger.error("🔥 Error saving contact: %s", e)
        else:
            logger.warning("Form Errors: %s", form.errors)
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import (
    Profile, SocialLink, TypedText, Fact, Skill, 
    Education, Certification, Experience, Project, Service
)
from .forms import ContactForm

def home(request):
    profile = Profile.objects.first()
    social_links = SocialLink.objects.all()
    typed_texts = TypedText.objects.all()
    facts = Fact.objects.all()
    skills = Skill.objects.all()
    educations = Education.objects.all()
    certifications = Certification.objects.all()
    experiences = Experience.objects.all().prefetch_related('details')
    projects = Project.objects.all()
    services = Service.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('home')
        else:
            messages.error(request, "There was an error in your message. Please try again.")
    else:
        form = ContactForm()

    context = {
        'profile': profile,
        'social_links': social_links,
        'typed_texts': typed_texts,
        'facts': facts,
        'skills': skills,
        'educations': educations,
        'certifications': certifications,
        'experiences': experiences,
        'projects': projects,
        'services': services,
        'form': form,
    }
    return render(request, 'portfolio/index.html', context)

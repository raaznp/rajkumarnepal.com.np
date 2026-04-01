from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm, UserProfileUpdateForm, ProfileForm, ProjectForm, SkillForm, ExperienceForm, EducationForm, CertificationForm, ServiceForm, SocialLinkForm, TypedTextForm, FactForm
from users.models import CustomUser
from portfolio.models import Profile, Project, Skill, Experience, ContactMessage

def is_superuser(user):
    return user.is_superuser

@login_required
def dashboard_home(request):
    """Main dashboard overview with statistics."""
    stats = {
        'total_projects': Project.objects.count(),
        'total_skills': Skill.objects.count(),
        'total_experiences': Experience.objects.count(),
        'unread_messages': ContactMessage.objects.filter(is_read=False).count() if hasattr(ContactMessage, 'is_read') else ContactMessage.objects.count()
    }
    return render(request, 'dash/index.html', {'stats': stats})

@login_required
@user_passes_test(is_superuser)
def user_list(request):
    """List of all dashboard users."""
    users = CustomUser.objects.all()
    return render(request, 'dash/user_list.html', {'users': users})

@login_required
@user_passes_test(is_superuser)
def add_user(request):
    """Internal view for superusers to create new dashboard users."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New user created successfully!')
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'dash/user_form.html', {'form': form, 'title': 'Add New User'})

@login_required
@user_passes_test(is_superuser)
def edit_user(request, pk):
    """View to update existing user details."""
    user_obj = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=user_obj)
        if form.is_valid():
            form.save()
            messages.success(request, f'User {user_obj.username} updated successfully!')
            return redirect('user_list')
    else:
        form = CustomUserChangeForm(instance=user_obj)
    return render(request, 'dash/user_form.html', {'form': form, 'title': f'Edit User: {user_obj.username}'})

@login_required
def account_settings(request):
    """View to allow logged-in users to update their own profile."""
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile settings have been updated!')
            return redirect('account_settings')
    else:
        form = UserProfileUpdateForm(instance=request.user)
    render_data = {
        'form': form,
        'title': 'Account Settings',
        'active_tab': 'settings'
    }
    return render(request, 'dash/settings.html', render_data)

@login_required
@user_passes_test(is_superuser)
def profile_info(request):
    """View to edit the global site profile info."""
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Portfolio profile updated successfully!')
            return redirect('profile_info')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'dash/user_form.html', {'form': form, 'title': 'Manage Portfolio Profile Info'})

# Project Management Views
@login_required
def project_list(request):
    """View to list all portfolio projects."""
    projects = Project.objects.all()
    return render(request, 'dash/project_list.html', {'projects': projects})

@login_required
def project_add(request):
    """View to add a new project."""
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project added successfully!')
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'dash/project_form.html', {'form': form, 'title': 'Add New Project'})

@login_required
def project_edit(request, pk):
    """View to edit an existing project."""
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, f'Project "{project.title}" updated successfully!')
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'dash/project_form.html', {'form': form, 'title': f'Edit Project: {project.title}'})

@login_required
def project_delete(request, pk):
    """View to delete a project."""
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        return redirect('project_list')
    return render(request, 'dash/confirm_delete.html', {'object': project, 'type': 'Project'})

# Skill Management Views
@login_required
def skill_list(request):
    """View to list all portfolio skills."""
    skills = Skill.objects.all().order_by('-percentage')
    return render(request, 'dash/skill_list.html', {'skills': skills})

@login_required
def skill_add(request):
    """View to add a new skill."""
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill added successfully!')
            return redirect('skill_list')
    else:
        form = SkillForm()
    return render(request, 'dash/skill_form.html', {'form': form, 'title': 'Add New Skill'})

@login_required
def skill_edit(request, pk):
    """View to edit an existing skill."""
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, f'Skill "{skill.name}" updated successfully!')
            return redirect('skill_list')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'dash/skill_form.html', {'form': form, 'title': f'Edit Skill: {skill.name}'})

@login_required
def skill_delete(request, pk):
    """View to delete a skill."""
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill deleted successfully!')
        return redirect('skill_list')
    return render(request, 'dash/confirm_delete.html', {'object': skill, 'type': 'Skill'})

# Experience Management Views
@login_required
def experience_list(request):
    """View to list all portfolio experiences."""
    experiences = Experience.objects.all().order_by('-duration')
    return render(request, 'dash/experience_list.html', {'experiences': experiences})

@login_required
def experience_add(request):
    """View to add a new experience."""
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Experience added successfully!')
            return redirect('experience_list')
    else:
        form = ExperienceForm()
    return render(request, 'dash/experience_form.html', {'form': form, 'title': 'Add New Experience'})

@login_required
def experience_edit(request, pk):
    """View to edit an existing experience."""
    exp = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
            messages.success(request, f'Experience at "{exp.company}" updated successfully!')
            return redirect('experience_list')
    else:
        form = ExperienceForm(instance=exp)
    return render(request, 'dash/experience_form.html', {'form': form, 'title': f'Edit Experience: {exp.company}'})

@login_required
def experience_delete(request, pk):
    """View to delete an experience."""
    exp = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        exp.delete()
        messages.success(request, 'Experience deleted successfully!')
        return redirect('experience_list')
    return render(request, 'dash/confirm_delete.html', {'object': exp, 'type': 'Experience'})

# Education & Certification views
@login_required
def education_list(request):
    """View to list both education and certifications."""
    educations = Education.objects.all()
    certs = Certification.objects.all()
    return render(request, 'dash/education_list.html', {'educations': educations, 'certs': certs})

@login_required
def education_add(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Education entry added!')
            return redirect('education_list')
    else:
        form = EducationForm()
    return render(request, 'dash/academic_form.html', {'form': form, 'title': 'Add Education'})

@login_required
def education_edit(request, pk):
    edu = get_object_or_404(Education, pk=pk)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=edu)
        if form.is_valid():
            form.save()
            messages.success(request, 'Education entry updated!')
            return redirect('education_list')
    else:
        form = EducationForm(instance=edu)
    return render(request, 'dash/academic_form.html', {'form': form, 'title': 'Edit Education'})

@login_required
def education_delete(request, pk):
    edu = get_object_or_404(Education, pk=pk)
    if request.method == 'POST':
        edu.delete()
        messages.success(request, 'Education entry deleted!')
        return redirect('education_list')
    return render(request, 'dash/confirm_delete.html', {'object': edu, 'type': 'Education'})

@login_required
def certification_add(request):
    if request.method == 'POST':
        form = CertificationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Certification added!')
            return redirect('education_list')
    else:
        form = CertificationForm()
    return render(request, 'dash/academic_form.html', {'form': form, 'title': 'Add Certification'})

@login_required
def certification_edit(request, pk):
    cert = get_object_or_404(Certification, pk=pk)
    if request.method == 'POST':
        form = CertificationForm(request.POST, instance=cert)
        if form.is_valid():
            form.save()
            messages.success(request, 'Certification updated!')
            return redirect('education_list')
    else:
        form = CertificationForm(instance=cert)
    return render(request, 'dash/academic_form.html', {'form': form, 'title': 'Edit Certification'})

@login_required
def certification_delete(request, pk):
    cert = get_object_or_404(Certification, pk=pk)
    if request.method == 'POST':
        cert.delete()
        messages.success(request, 'Certification deleted!')
        return redirect('education_list')
    return render(request, 'dash/confirm_delete.html', {'object': cert, 'type': 'Certification'})

# Services & Social Links views
@login_required
def service_list(request):
    """View to list both services and social links."""
    services = Service.objects.all()
    socials = SocialLink.objects.all()
    return render(request, 'dash/services_list.html', {'services': services, 'socials': socials})

@login_required
def service_add(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service added!')
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'dash/user_form.html', {'form': form, 'title': 'Add Service'})

@login_required
def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service updated!')
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'dash/user_form.html', {'form': form, 'title': 'Edit Service'})

@login_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        messages.success(request, 'Service deleted!')
        return redirect('service_list')
    return render(request, 'dash/confirm_delete.html', {'object': service, 'type': 'Service'})

@login_required
def social_add(request):
    if request.method == 'POST':
        form = SocialLinkForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Social link added!')
            return redirect('service_list')
    else:
        form = SocialLinkForm()
    return render(request, 'dash/user_form.html', {'form': form, 'title': 'Add Social Link'})

@login_required
def social_edit(request, pk):
    social = get_object_or_404(SocialLink, pk=pk)
    if request.method == 'POST':
        form = SocialLinkForm(request.POST, instance=social)
        if form.is_valid():
            form.save()
            messages.success(request, 'Social link updated!')
            return redirect('service_list')
    else:
        form = SocialLinkForm(instance=social)
    return render(request, 'dash/user_form.html', {'form': form, 'title': 'Edit Social Link'})

@login_required
def social_delete(request, pk):
    social = get_object_or_404(SocialLink, pk=pk)
    if request.method == 'POST':
        social.delete()
        messages.success(request, 'Social link deleted!')
        return redirect('service_list')
    return render(request, 'dash/confirm_delete.html', {'object': social, 'type': 'Social Link'})

# Personalization views (Typed Text & Facts)
@login_required
def personalization_list(request):
    """View to list both typed texts and facts."""
    typed_texts = TypedText.objects.all()
    facts = Fact.objects.all()
    return render(request, 'dash/personalization_list.html', {'typed_texts': typed_texts, 'facts': facts})

@login_required
def typed_text_add(request):
    if request.method == 'POST':
        form = TypedTextForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Typed text highlight added!')
            return redirect('personalization_list')
    else:
        form = TypedTextForm()
    return render(request, 'dash/user_form.html', {'form': form, 'title': 'Add Typed Text Highlight'})

@login_required
def typed_text_edit(request, pk):
    item = get_object_or_404(TypedText, pk=pk)
    if request.method == 'POST':
        form = TypedTextForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Typed text highlight updated!')
            return redirect('personalization_list')
    else:
        form = TypedTextForm(instance=item)
    return render(request, 'dash/user_form.html', {'form': form, 'title': 'Edit Typed Text Highlight'})

@login_required
def typed_text_delete(request, pk):
    item = get_object_or_404(TypedText, pk=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Typed text highlight deleted!')
        return redirect('personalization_list')
    return render(request, 'dash/confirm_delete.html', {'object': item, 'type': 'Typed Text Highlight'})

@login_required
def fact_add(request):
    if request.method == 'POST':
        form = FactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fact added!')
            return redirect('personalization_list')
    else:
        form = FactForm()
    return render(request, 'dash/user_form.html', {'form': form, 'title': 'Add Portfolio Fact'})

@login_required
def fact_edit(request, pk):
    fact = get_object_or_404(Fact, pk=pk)
    if request.method == 'POST':
        form = FactForm(request.POST, instance=fact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fact updated!')
            return redirect('personalization_list')
    else:
        form = FactForm(instance=fact)
    return render(request, 'dash/user_form.html', {'form': form, 'title': 'Edit Portfolio Fact'})

@login_required
def fact_delete(request, pk):
    fact = get_object_or_404(Fact, pk=pk)
    if request.method == 'POST':
        fact.delete()
        messages.success(request, 'Fact deleted!')
        return redirect('personalization_list')
    return render(request, 'dash/confirm_delete.html', {'object': fact, 'type': 'Fact'})

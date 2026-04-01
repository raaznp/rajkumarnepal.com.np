from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm, UserProfileUpdateForm, ProfileForm, ProjectForm, SkillForm
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

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm, UserProfileUpdateForm
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

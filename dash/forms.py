from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser

from portfolio.models import Profile, Project, Skill, Experience, Education, Certification, Service, SocialLink

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'intro_text': forms.Textarea(attrs={'rows': 3}),
            'about_text': forms.Textarea(attrs={'rows': 5}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        widgets = {
            'percentage': forms.NumberInput(attrs={'max': 100, 'min': 0}),
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class SocialLinkForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = '__all__'

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_picture')

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'profile_picture')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'profile_picture', 'first_name', 'last_name', 'is_staff', 'is_active')

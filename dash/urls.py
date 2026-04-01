from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dash_home'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Password Reset
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), 
         name='password_reset'),
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), 
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), 
         name='password_reset_confirm'),
    path('password-reset-complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), 
         name='password_reset_complete'),
         
    # Internal User Management
    path('users/', views.user_list, name='user_list'),
    path('users/add/', views.add_user, name='add_user'),
    path('users/edit/<int:pk>/', views.edit_user, name='edit_user'),
    
    # Account Settings
    path('settings/', views.account_settings, name='account_settings'),
    
    # Portfolio Management
    path('portfolio/profile/', views.profile_info, name='profile_info'),
    
    # Projects CRUD
    path('portfolio/projects/', views.project_list, name='project_list'),
    path('portfolio/projects/add/', views.project_add, name='project_add'),
    path('portfolio/projects/edit/<int:pk>/', views.project_edit, name='project_edit'),
    path('portfolio/projects/delete/<int:pk>/', views.project_delete, name='project_delete'),
    
    # Skills CRUD
    path('portfolio/skills/', views.skill_list, name='skill_list'),
    path('portfolio/skills/add/', views.skill_add, name='skill_add'),
    path('portfolio/skills/edit/<int:pk>/', views.skill_edit, name='skill_edit'),
    path('portfolio/skills/delete/<int:pk>/', views.skill_delete, name='skill_delete'),
    
    # Experience CRUD
    path('portfolio/experience/', views.experience_list, name='experience_list'),
    path('portfolio/experience/add/', views.experience_add, name='experience_add'),
    path('portfolio/experience/edit/<int:pk>/', views.experience_edit, name='experience_edit'),
    path('portfolio/experience/delete/<int:pk>/', views.experience_delete, name='experience_delete'),
    
    # Education CRUD
    path('portfolio/education/', views.education_list, name='education_list'),
    path('portfolio/education/add/', views.education_add, name='education_add'),
    path('portfolio/education/edit/<int:pk>/', views.education_edit, name='education_edit'),
    path('portfolio/education/delete/<int:pk>/', views.education_delete, name='education_delete'),
    
    # Certification CRUD
    path('portfolio/certification/add/', views.certification_add, name='certification_add'),
    path('portfolio/certification/edit/<int:pk>/', views.certification_edit, name='certification_edit'),
    path('portfolio/certification/delete/<int:pk>/', views.certification_delete, name='certification_delete'),
    
    # Services CRUD
    path('portfolio/services/', views.service_list, name='service_list'),
    path('portfolio/services/add/', views.service_add, name='service_add'),
    path('portfolio/services/edit/<int:pk>/', views.service_edit, name='service_edit'),
    path('portfolio/services/delete/<int:pk>/', views.service_delete, name='service_delete'),
    
    # Social Links CRUD
    path('portfolio/social/add/', views.social_add, name='social_add'),
    path('portfolio/social/edit/<int:pk>/', views.social_edit, name='social_edit'),
    path('portfolio/social/delete/<int:pk>/', views.social_delete, name='social_delete'),
    
    # Personalization CRUD
    path('portfolio/personalization/', views.personalization_list, name='personalization_list'),
    path('portfolio/typed-text/add/', views.typed_text_add, name='typed_text_add'),
    path('portfolio/typed-text/edit/<int:pk>/', views.typed_text_edit, name='typed_text_edit'),
    path('portfolio/typed-text/delete/<int:pk>/', views.typed_text_delete, name='typed_text_delete'),
    path('portfolio/fact/add/', views.fact_add, name='fact_add'),
    path('portfolio/fact/edit/<int:pk>/', views.fact_edit, name='fact_edit'),
    path('portfolio/fact/delete/<int:pk>/', views.fact_delete, name='fact_delete'),
    
    # Communication (Contact Messages)
    path('portfolio/messages/', views.message_list, name='message_list'),
    path('portfolio/messages/<int:pk>/', views.message_detail, name='message_detail'),
    path('portfolio/messages/delete/<int:pk>/', views.message_delete, name='message_delete'),
]

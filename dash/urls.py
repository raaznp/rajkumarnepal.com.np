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
]

from django.contrib import admin
from .models import (
    Profile, SocialLink, TypedText, Fact, Skill, 
    Education, Certification, Experience, ExperienceDetail, 
    Project, Service, ContactMessage
)

class ExperienceDetailInline(admin.TabularInline):
    model = ExperienceDetail
    extra = 1

class ExperienceAdmin(admin.ModelAdmin):
    inlines = [ExperienceDetailInline]

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'timestamp')
    readonly_fields = ('name', 'email', 'subject', 'message', 'timestamp')

admin.site.register(Profile)
admin.site.register(SocialLink)
admin.site.register(TypedText)
admin.site.register(Fact)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Project)
admin.site.register(Service)

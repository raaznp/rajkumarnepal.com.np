from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    intro_text = models.TextField()
    about_text = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    website = models.URLField()
    degree = models.CharField(max_length=100)
    profession = models.CharField(max_length=100, blank=True, null=True)
    freelance_status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name

class SocialLink(models.Model):
    platform = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=50)  # e.g., fa-facebook
    url = models.URLField()

    def __str__(self):
        return self.platform

class TypedText(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text

class Fact(models.Model):
    icon_class = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Education(models.Model):
    degree = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    institution = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Education"

    def __str__(self):
        return self.degree

class Certification(models.Model):
    name = models.CharField(max_length=200)
    date = models.CharField(max_length=50)
    issuer = models.CharField(max_length=100)
    verification_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Experience(models.Model):
    role = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Experience"

    def __str__(self):
        return f"{self.role} at {self.company}"

class ExperienceDetail(models.Model):
    experience = models.ForeignKey(Experience, related_name='details', on_delete=models.CASCADE)
    detail = models.TextField()

    def __str__(self):
        return f"Detail for {self.experience.role}"

class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/')
    description = models.TextField()
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Service(models.Model):
    icon_class = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    @property
    def profile_image_url(self):
        """Returns the profile picture URL safely."""
        try:
            if self.profile_picture and hasattr(self.profile_picture, 'url'):
                return self.profile_picture.url
        except Exception:
            pass
        return None

    def __str__(self):
        return self.username

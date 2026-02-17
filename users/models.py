from django.conf import settings
from django.db import models

from cloudinary.models import CloudinaryField


class Profile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    location = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    profile_image = CloudinaryField("image", blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Profile: {self.user}"

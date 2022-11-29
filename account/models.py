from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):
    """User Profile OneToOne with admin user."""

    # Create relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add additional attributes
    phone = models.CharField(max_length=265)
    address = models.CharField(max_length=265)

    def __str__(self):
        return self.user.username

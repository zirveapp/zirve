from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import Interest


class CustomUser(AbstractUser):
    interests = models.ForeignKey(Interest, on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
from django.db import models


class UserProfile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    city = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name_plural = "users"

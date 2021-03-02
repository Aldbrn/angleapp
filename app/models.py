from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="photos")
    fish = models.CharField(max_length=20)
    size = models.PositiveIntegerField(null=True, blank=True)
    comment = models.TextField(blank=True)
    pref = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.fish

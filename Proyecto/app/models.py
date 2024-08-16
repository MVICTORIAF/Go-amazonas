from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')
    name = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'












  


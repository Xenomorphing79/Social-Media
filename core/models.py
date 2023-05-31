from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userId = models.IntegerField()
    bio = models.TextField(blank=True)
    profileImg = models.ImageField(upload_to='profileImages', default='default.png')
    location = models.CharField(max_length=50, blank=True)
    createdAt = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='postImages')
    caption = models.TextField()
    createdAt = models.DateTimeField(default=datetime.now)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)
    
class LikePost(models.Model):
    post_id = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)
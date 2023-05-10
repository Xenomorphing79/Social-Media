from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userId = models.IntegerField()
    bio = models.TextField(blank=True)
    profileImg = models.ImageField(upload_to='profileImages', default='icons8-customer-50ac0359ca-4a3f-48e9-bf84-825a3fe383d2.png')
    location = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username
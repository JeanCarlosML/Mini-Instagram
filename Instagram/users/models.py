from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # URLFiel = CharField con algunas validaciones
    website = models.URLField(max_length=200, blank=True)
    bigoraphy = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    #Necesitamos libreria Pillow
    picture = models.ImageField(upload_to="users/picture", blank=True, null=True)
    #Cuando se crea auto_now_add
    created = models.DateTimeField(auto_now_add=True)
    #Cada vez que es modificado auto_now
    modified = models.DateTimeField(auto_now=True)
    pass

    def __str__(self):
        return self.user.username
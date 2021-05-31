from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/image/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
from django.db import models

# Create your models here.

class User_picture(models.Model):

    user_name = models.CharField(max_length=50)

    user_image = models.ImageField(upload_to='image/')
    user_image_after = models.CharField(max_length=100)
    upload_time = models.DateTimeField()
    #introduce = models.FileField(upload_to='introduce/')
    
    def __str__(self):
        return self.user_name

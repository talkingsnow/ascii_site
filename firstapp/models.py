from django.db import models

class DB_Image(models.Model):
    image = models.ImageField(upload_to="images")
    text = models.TextField()

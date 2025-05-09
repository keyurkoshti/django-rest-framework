from django.db import models

# Create your models here.
class userData(models.Model):
    username=models.CharField(max_length=150, unique=True)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.username
    
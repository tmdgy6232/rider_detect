from django.db import models

# Create your models here.

class Detect(models.Model):
    classification_type = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to='detect/', null=False)
    created_at = models.DateField(auto_now_add=True, null=False)

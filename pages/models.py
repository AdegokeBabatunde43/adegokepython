from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    data= models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title

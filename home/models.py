from django.db import models

# Create your models here.
# model defines the db
class Contact(models.Model):   #stores information into the db
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    
    def __str__(self) -> str:
        return self.name


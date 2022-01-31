from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    addres = models.TextField
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

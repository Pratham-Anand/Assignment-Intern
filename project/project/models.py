from django.db import models

class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

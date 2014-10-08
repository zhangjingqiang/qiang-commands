from django.db import models

class Command(models.Model):
    title = models.CharField(max_length=200)
    command = models.TextField()

    def __str__(self):
        return self.command
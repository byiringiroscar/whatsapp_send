from django.db import models


# Create your models here.


class MessageSend(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'{self.title}'

from django.db import models

# Create your models here.

class NotMessages(models.Model):
    jid_to = models.CharField(max_length=200)
    jid_from = models.CharField(max_length=200)
    message = models.CharField(max_length=200)

    def __str__(self):
        return "to: " + self.jid_to + " from: " + self.jid_from + " message: " + self.message

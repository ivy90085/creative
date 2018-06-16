from django.db import models

class Message(models.Model):
        user = models.CharField(max_length=50)
        subject = models.CharField(max_length=200)

        def __unicode__(self):
                return self.subject
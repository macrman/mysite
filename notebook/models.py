from django.db import models


class TextNote(models.Model):
    is_published = models.BooleanField()
    content = models.TextField()
    pub_date = models.DateTimeField(null=True, blank=True)

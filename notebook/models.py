import datetime

from django.db import models
from django.utils.timezone import utc


class TextNote(models.Model):
    is_published = models.BooleanField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.is_published and not self.pub_date:
            self.pub_date = datetime.datetime.utcnow().replace(tzinfo=utc)
        super(TextNote, self).save(*args, **kwargs)


from django.db import models
from django.db.models import Max

from int_to_36 import int_to_36


class ShortUrl(models.Model):
    source_url = models.URLField('source url', max_length=8192)
    short_url = models.CharField('short url', max_length=128, blank=True, null=True)
    created = models.DateTimeField('created', auto_now_add=True, blank=True, null=True, editable=False, default=0)
    clicks = models.PositiveIntegerField('clicks', default=0, blank=True, null=True)

    class Meta():
        verbose_name = 'short url'
        verbose_name_plural = 'short urls'

    def __unicode__(self):
        return '%s (%s)' % (self.source_url[0:50], self.short_url)

    def save(self, *args, **kwargs):
        last_object = ShortUrl.objects.all().aggregate(Max('pk'))
        next_pk = last_object['pk__max'] or 0 + 1
        self.short_url = int_to_36(next_pk)
        super(ShortUrl, self).save(*args, **kwargs)

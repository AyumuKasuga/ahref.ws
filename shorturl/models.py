from django.db import models
from django.db.models import Max

from int_to_36 import int_to_36


class ShortUrl(models.Model):
    source_url = models.URLField('source url', max_length=8192)
    short_url_int = models.PositiveIntegerField('short url int', default=0, blank=True, null=True, unique=True)
    short_url = models.CharField('short url', max_length=128, blank=True, null=True, unique=True)
    created = models.DateTimeField('created', auto_now_add=True, blank=True, null=True, editable=False, default=0)
    clicks = models.PositiveIntegerField('clicks', default=0, blank=True, null=True)

    class Meta():
        verbose_name = 'short url'
        verbose_name_plural = 'short urls'


    def __unicode__(self):
        return '%s (%s)' % (self.source_url[0:50], self.short_url)

    def save(self, *args, **kwargs):
        if not self.pk:
            last_object = ShortUrl.objects.all().aggregate(Max('short_url_int'))
            self.short_url_int = (last_object['short_url_int__max'] or 0) + 1
            self.short_url = int_to_36(self.short_url_int)
        super(ShortUrl, self).save(*args, **kwargs)

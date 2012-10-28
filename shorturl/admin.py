from django.contrib import admin
from shorturl import models

class ShortUrlAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(models.ShortUrl, ShortUrlAdmin)

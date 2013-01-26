from django.db import models


class Link(models.Model):
    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    def __unicode__(self):
        pass

    clicks = models.IntegerField(default=0)
    url = models.URLField(blank=True, max_length=512)
    code = models.CharField(default="", max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def generate_code(self):
        pass

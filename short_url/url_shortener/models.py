from django.db import models


class Link(models.Model):
    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    def __unicode__(self):
        pass

    clicks = models.IntegerField(default=0)
    url = models.URLField(blank=True)
    code = models.CharField(default="", max_length=10)

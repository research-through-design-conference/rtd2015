from django.db import models
from django.core.urlresolvers import reverse


class Home(models.Model):

    title = models.CharField(max_length=200)
    text = models.TextField()
    header_image = models.FileField(upload_to='page/%Y/%m/%d', null=True, blank=True)

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('site_2015.views.home')


class Page(models.Model):

    title = models.CharField(max_length=200)
    nav_text = models.CharField(max_length=30, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=255, null=True, blank=True)
    text = models.TextField()
    header_image = models.FileField(upload_to='page/%Y/%m/%d', null=True, blank=True)
    pub_date = models.DateTimeField(null=True, blank=True)
    top_level_nav = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('site_2015.views.page', args=[self.slug])


class HomeImg(models.Model):
    home = models.ForeignKey('Home', related_name='images')
    image = models.FileField(upload_to='page/%Y/%m/%d', null=True, blank=True)


class PageImg(models.Model):
    page = models.ForeignKey('Page', related_name='images')
    image = models.FileField(upload_to='page/%Y/%m/%d', null=True, blank=True)

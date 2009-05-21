"""
    Category Models
"""

from django.db import models
from toolbox.fields import AutoSlugField
from django.template.defaultfilters import slugify
import mptt

class Category(models.Model):
    """Category Model holds information about our heirarchy"""

    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=255)
    slug = AutoSlugField(max_length=100, blank=True, unique=True,
        populate_from='name', editable=True)

    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    priority = models.IntegerField(default=0)

    parent = models.ForeignKey('self', null=True, blank=True,
        related_name='children')

    def __unicode__(self):
        return " > ".join([cat.name for cat in self.get_heirarchy()])

    def get_heirarchy(self):
        """Return the ancestors plus the current category"""

        items = list(self.get_ancestors())
        items.append(self)

        return items

    @property
    def full_slug(self):
        """Return the full slug for this category"""
        return "/".join([cat.slug for cat in self.get_heirarchy()])

    def get_absolute_url(self):
        """Return URL for this instance"""
        return "/category/%s.html" % self.full_slug

    def save(self, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super(Category, self).save(**kwargs)



# Open Bug: http://code.google.com/p/django-mptt/issues/detail?id=14
try:
    mptt.register(Category, order_insertion_by=['name'])
except mptt.AlreadyRegistered:
    pass

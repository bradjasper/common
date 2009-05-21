"""Common model fields"""
import re
from django.db import models

def slugify(data):
    """Turn a piece of data into a slug"""

    data = data.lower()
    data = re.sub('\s+', '-', data)
    data = data.replace('--', '-', data)
    data = data.replace('--', '-', data)
    return re.sub('[^a-z0-9\-]', '', data)

class Common(models.Model):
    """Common base for handling things like saving slugs.
    We don't put fields in here because Django puts those in seperate
    tables."""

    class Meta:
        abstract = True

    def save(self):
        if hasattr(self, 'slug'):
            if self.slug is None or len(self.slug.strip()) == 0:
                self.slug = slugify(self.name)

        super(Common, self).save()

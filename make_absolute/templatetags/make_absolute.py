from django.conf import settings

from django.template.defaultfilters import stringfilter
from django.template import Library

register = Library()

@register.filter(name="make_absolute")
@stringfilter
def make_absolute(value):
    """Convert a relative path to an absolute path"""

    if hasattr(settings, "ROOT_URL"):

        # Replace relative paths with absolute paths
        return value.replace(
            'href="/',
            'href="%s' % settings.ROOT_URL
        )

    return value

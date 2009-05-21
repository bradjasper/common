from django.shortcuts import get_object_or_404

from models import Category
from templates import Template

template = Template()

def get_slugs(slug):
    """Return a parent and a child slug given a string.

    boom/town.html -> (boom, town)
    boom/blah/town.html -> (blah, town)
    boom.html -> (None, boom)"""

    parent = None
    parts = slug.split("/")
    child = parts[-1]

    if len(parts) > 1:
        parent = parts[-2]

    return (parent, child)


def category(request, slug):
    """Show an individual category"""


    if slug:
        parent, child = get_slugs(slug)

        if parent:
            parent = Category.objects.get(slug=parent)

        category = get_object_or_404(Category, slug=child, parent=parent)
        children = category.get_children()

    # Main page
    else:
        category = None
        children = Category.objects.filter(parent=None)



    return template.render_to_response('categories/category.html', {
        'category': category,
        'children': children})

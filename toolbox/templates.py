"""
    Templates is a basic template engine using jinja. It simplifies
    creation and rendering of templates.
"""

import jinja2

from django import http

class Template(object):

    def __init__(self, package, directory):
        """Name of the package this template belongs to, and the relative
        directory inside that package where templates can be found"""

        self.env = jinja2.Environment(extensions=['jinja2.ext.loopcontrols'],
            loader=jinja2.PackageLoader(package, directory))

    def render_to_response(self, template, context = None):

        if context is None:
            context = {}

        obj = self.env.get_template(template)
        contents = obj.render(**context)

        return http.HttpResponse(contents)

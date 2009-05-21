from django.db import models

class Action(models.Model):
    """Action is the base for other analytics to build off."""

    ip = models.IPAddressField()

    class Meta:
        abstract = True

class Impression(Action):
    """Impression is an analytics term that refers to a single view. If
    something has 10 impressions, its been viewed 10 times"""


class Click(Action):
    """Click is an analytics term that refers to a single mouse click or
    action"""
    

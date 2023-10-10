from django.db import models

class Thing(models.Model):
    """name: a short string that identifies a thing.
        description: a slightly longer string that describes a thing.
        quantity: an integer that identifies the number of items of a thing we possess."""
    
    name = models.CharField()
    description =  models.CharField()
    quantity = models.IntegerField()
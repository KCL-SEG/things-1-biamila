from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
class Thing(models.Model):
    """name: a short string that identifies a thing.
        description: a slightly longer string that describes a thing.
        quantity: an integer that identifies the number of items of a thing we possess."""
    """
        name must be unique, must not be blank, and must consist of 30 characters or less.
        description need not be unique, may be blank, and must consist of 120 characters of less.
        quantity need not be unique, and must be an integer value between 0 and 100 (inclusive). 
            quantity may be 0 and it may be 100, but not less than 0 and not more than 100
    """
    name = models.CharField(
        unique=True,
        blank=False,
        max_length=30
    )

    description =  models.CharField(
        unique=False,
        blank=True,
        max_length=120
    )

    quantity = models.IntegerField(
        unique=False,
        validators=[MaxValueValidator(100),
                    MinValueValidator(0)]
    )
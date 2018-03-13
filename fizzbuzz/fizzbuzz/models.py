import random
import string

from django.db import models
from django.utils.translation import gettext_lazy as _

# Length of the string for unique Generator url:
HASH_LENGTH = 10


class Generator(models.Model):

    name = models.CharField(max_length=20)
    results_per_generator = models.IntegerField(
        help_text=_(
            'Since the length of generated string for a generator is '
            'unlimited, we have to set a maximum numberof results to return. '
        )
    )
    hash_for_url = models.CharField(
        blank=True,
        max_length=HASH_LENGTH,
        help_text=_(
            'This field will be generated automatically when saving the '
            'Generator'
        )
    )

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):

        if not self.hash_for_url:
            ''.join(
                random.choice(string.ascii_letters) for m in range(HASH_LENGTH)
            )

        super(Generator, self).save(*args, **kwargs)


class Divisor(models.Model):
    number = models.IntegerField()
    generator = models.ForeignKey(Generator)

    def __unicode__(self):
        return self.number


class String(models.Model):
    string_to_append = models.IntegerField()
    generator = models.ForeignKey(Generator)

    def __unicode__(self):
        return self.string_to_append

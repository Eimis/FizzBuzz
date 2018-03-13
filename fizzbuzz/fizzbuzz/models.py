from django.db import models
from django.utils.translation import gettext_lazy as _


class Generator(models.Model):
    name = models.CharField(max_length=20)
    results_per_generator = models.IntegerField(
        help_text=_(
            'Since the length of generated string for a generator is '
            'unlimited, we have to set a maximum numberof results to return. '
        )
    )

    def __unicode__(self):
        return self.name


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

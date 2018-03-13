from django.db import models


class Generator(models.Model):
    name = models.CharField(max_length=20)

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

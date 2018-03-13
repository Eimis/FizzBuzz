from django.contrib import admin
from fizzbuzz.models import Generator


class GeneratorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Generator, GeneratorAdmin)

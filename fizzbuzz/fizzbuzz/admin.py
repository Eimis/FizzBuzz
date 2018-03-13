from django.contrib import admin
from fizzbuzz.models import Divisor, Generator, String


class DivisorAdmin(admin.ModelAdmin):
    pass


class GeneratorAdmin(admin.ModelAdmin):
    pass


class StringAdmin(admin.ModelAdmin):
    pass

admin.site.register(Divisor, DivisorAdmin)
admin.site.register(Generator, GeneratorAdmin)
admin.site.register(String, StringAdmin)

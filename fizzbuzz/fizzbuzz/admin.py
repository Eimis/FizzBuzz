from django.contrib import admin
from fizzbuzz.models import Divisor, Generator, String


class DivisorAdmin(admin.ModelAdmin):
    pass


class GeneratorAdmin(admin.ModelAdmin):
    readonly_fields = ('hash_for_url', )


class StringAdmin(admin.ModelAdmin):
    pass

admin.site.register(Divisor, DivisorAdmin)
admin.site.register(Generator, GeneratorAdmin)
admin.site.register(String, StringAdmin)

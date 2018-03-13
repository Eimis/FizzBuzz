from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from fizzbuzz.models import Generator


def main(request):
    '''Main app view
    '''

    return render(request, 'main.html', {
        'generators': Generator.objects.all(),
    })


def generator_view(request, hash_for_url):
    '''A view for using Generator and generating sequences
    '''

    errors = None
    generator = Generator.objects.filter(hash_for_url=hash_for_url).first()

    if not generator:
        errors = _("Generator with such URL doesn't exist!")

    return render(request, 'generator.html', {
        'errors': errors,
        'generator': generator,
    })

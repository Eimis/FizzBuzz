from django.shortcuts import render

from fizzbuzz.models import Generator


def main(request):
    '''Main app view
    '''

    return render(request, 'main.html', {
        'generators': Generator.objects.all(),
    })

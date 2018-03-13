from django.conf.urls import url
from django.contrib import admin

from fizzbuzz.views import generator_view, main

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main),
    url(
        r'^generator/(?P<hash_for_url>.*)$',
        generator_view,
        name='generator_view'
    ),
]

from django.conf.urls import url
from django.contrib import admin

from fizzbuzz.views import main

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main),
]

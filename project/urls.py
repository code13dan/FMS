"""FMS URL Configuration"""

from django.conf.urls import url, include
from django.contrib import admin

from partners.urls import urlpatterns as partners_urls
from invoices.urls import urlpatterns as invoices_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^partners/', include(partners_urls, namespace='partners-app')),
    url(r'^invoices/', include(invoices_urls, namespace='invoices-app')),
]

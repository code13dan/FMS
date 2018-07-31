"""Partners app's urls"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^all$', views.all_partners, name='all-url'),
    url(r'^add$', views.add_partner, name='add-url'),
    url(r'^show/(\d+)$', views.show_partner, name='show-url'),
    url(r'^edit/(\d+)$', views.edit_partner, name='edit-url'),
    url(r'^delete/(\d+)$', views.delete_partner, name='delete-url'),
    url(r'^get/(\d+)$', views.get_partner, name='get-url'),
]

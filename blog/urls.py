from django.conf.urls import url
from .views import IndexPage, AboutPage, contact_page

urlpatterns = [
    url(r'^$', IndexPage.as_view(), name='index'),
    url(r'^about/$', AboutPage.as_view(), name='about'),
    url(r'^contact/$', contact_page, name='contact'),
]
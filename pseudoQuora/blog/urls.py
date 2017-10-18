from django.conf.urls import url,include

from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^ask/$',views.ask),
    url(r'^log-in/$',views.login),
    url(r'^contact/$',views.contact)
]

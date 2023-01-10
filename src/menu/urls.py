from django.urls import path, reverse_lazy
from menu.views import getMenu
from menu.models import TreeMenu
from django.views.generic import RedirectView

urlpatterns = []
urlpatterns.append( path('', RedirectView.as_view(url=reverse_lazy('home'))))
for url_object in TreeMenu.objects.all():
    urlpatterns.append( path(url_object.link+"/", getMenu, {'name': url_object.name}, name=url_object.link))

from django.conf.urls import url
from . import views
app_name = 'classroom'
urlpatterns = [
    #/music/
    url(r'^$', views.index, name='index'),
    url(r'^calculate/$', views.calculate, name='calculate'),



]



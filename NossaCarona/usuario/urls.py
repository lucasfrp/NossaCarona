from django.conf.urls import patterns, include, url

urlpatterns = patterns('usuario.views', 
    url(r'^login/$', 'login'),
    url(r'^logout/$', 'logout'),
    url(r'^novousuario/$', 'novousuario'),
)

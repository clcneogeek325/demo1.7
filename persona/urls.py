from django.conf.urls import patterns, include, url

urlpatterns = patterns('persona.views',
    # Examples:

    url(r'^$', 'lista_personas', name='home'),
    url(r'^form/$', 'formulario', name='form'),
)

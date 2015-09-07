from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^$', 'pikquick.views.inicio', name='inicio'),
                       url(r'^usuario/nuevo$','pikquick.views.nuevo_usuario', name='nuevo_usuario'),
                       url(r'^usuario/ingreso$','pikquick.views.ingreso_usuario', name='ingreso_usuario'),
                       url(r'^usuario/salir$','pikquick.views.salir_usuario', name='salir_usuario'),
                       url(r'^usuario/cambiar_pass$','pikquick.views.cambiar_pass', name='cambiar_pass'),
                       url(r'^ajustes$', 'pikquick.views.ajustes', name='ajustes'),
                      )

from django.urls import path

from funil_vagas.base.views import home

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
]

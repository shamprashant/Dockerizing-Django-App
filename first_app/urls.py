from django.conf.urls import url
from . import views

app_name = 'first_app'

urlpatterns = [
    url('^$', views.index, name = 'index'),
    url('^game/', views.start_game, name = 'game')
]
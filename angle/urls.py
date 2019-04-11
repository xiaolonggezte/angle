from django.conf.urls import include, url
from django.contrib import admin

from game import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'angle.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^(?P<type_id>[0-9]+)$', views.index, name='game_index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^angle/', include('game.urls')),
    url(r'^vivian/', views.data_list, name='data_list'),
]

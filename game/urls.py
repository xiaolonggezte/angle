from django.conf.urls import patterns, url

from game import views

urlpatterns = patterns(
    'game.views',
    url(r'^example', views.card_example, name='card_example'),
    url(r'^$', views.index, name='game_index'),
    url(r'^show$', views.cards_show, name='cards_show'),
    url(r'^wait/role_distribution/', views.role_distribution, name='role_distribution'),
    url(r'^wait/role/', views.role, name='role'),
    url(r'^poker/distribution/', views.poker_distribution, name='poker_distribution'),
    url(r'^data/note/', views.data_note, name='data_note'),
)
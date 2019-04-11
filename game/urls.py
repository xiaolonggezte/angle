from django.conf.urls import patterns, url

from game import views

urlpatterns = patterns(
    'game.views',
    url(r'^card/', views.card_example, name='get_ans'),
    url(r'^(?P<type_id>[0-9]+)$', views.index, name='game_index'),
    url(r'^show$', views.cards_show, name='cards_show'),
    url(r'^wait/role_distribution/', views.role_distribution, name='role_distribution'),
    url(r'^wait/role/', views.role, name='role'),
    url(r'^poker/distribution/', views.poker_distribution, name='poker_distribution'),
    url(r'^data/note/', views.data_note, name='data_note'),
    url(r'^update/db', views.update_db, name='update_db'),
    url(r'^finished', views.finished, name='finished'),
    url(r'^admin/data/list', views.data_list, name='data_list'),
    url(r'^admin/alter_mask', views.alter_mask, name='alter_mask'),
)
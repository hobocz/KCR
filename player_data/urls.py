from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


""" We only need Read operations

Endoints documented in the README
"""
urlpatterns = [
    path('', views.PlayerList.as_view(), name = 'player_list'),
    path('<int:id>/', views.PlayerDetail.as_view(), name = 'player_detail'),
    path('<int:id>/stats/', views.PlayerStats.as_view(), name = 'player_stats'),
    path('top-young-pitchers/', views.TopYoungPitchersView.as_view(), name = 'top_young_pitchers'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
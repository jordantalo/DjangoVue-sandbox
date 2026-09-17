from django.urls import path
from .views import get_players, create_player, player_detail
from .views import get_matches, create_match

urlpatterns = [
    path("players/", get_players),
	path("players/add", create_player),
	path("players/<int:pk>/", player_detail),
	path("matches/", get_matches),
	path("matches/add", create_match),
]

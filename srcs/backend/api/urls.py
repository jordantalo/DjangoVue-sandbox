from django.urls import path
from .views import get_players, create_player

urlpatterns = [
    path("players/", get_players),
	path("players/add", create_player),
]

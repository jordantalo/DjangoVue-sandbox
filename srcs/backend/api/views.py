from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Player, Match
from .serializers import PlayerSerializer, MatchSerializer

# Create your views here.
@api_view(["GET"])
def get_players(request):
	if request.method == "GET":
		players = Player.objects.all()
		serializer = PlayerSerializer(players, many=True)
		return Response(serializer.data)

	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def create_player(request):
	if request.method == "POST":
		data = JSONParser().parse(request)
		serializer = PlayerSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

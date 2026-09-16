from rest_framework import serializers
from .models import Player, Match

class PlayerSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	username = serializers.CharField(required=True, allow_blank=False, max_length=255)
	avatar_url = serializers.URLField(required=False)
	score = serializers.IntegerField(required=False)

	def create(self, validated_data):
		"""
        Create and return a new `Player` instance, given the validated data.
        """
		return Player.objects.create(**validated_data)

	def update(self, instance, validated_data):
		"""
        Update and return an existing `Player` instance, given the validated data.
        """
		instance.username = validated_data.get("username", instance.username)
		instance.avatar_url = validated_data.get("avatar_url", instance.avatar_url)
		instance.score = validated_data.get("score", instance.score)
		return instance

class MatchSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	player1 = serializers.IntegerField(required=True)
	player2 = serializers.IntegerField(required=True)
	score_p1 = serializers.IntegerField(required=True)
	score_p2 = serializers.IntegerField(required=True)

	def create(self, validated_data):
		"""
        Create and return a new `Match` instance, given the validated data.
        """
		return Match.objects.create(**validated_data)

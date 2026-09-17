from rest_framework import serializers
from .models import Player, Match

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

    def validate_score(self, value):
        # self.instance existe SEULEMENT lors d'un PUT/PATCH (mise à jour)
        # self.instance est None lors d'un POST (création)
        if self.instance is not None and value != self.instance.score:
            raise serializers.ValidationError("Le score ne peut pas être modifié directement via la mise à jour du profil !")
        return value

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'  # Exporte/importe TOUS les champs du modèle Match
        read_only_fields = ['p1_username_snapshot', 'p2_username_snapshot']
